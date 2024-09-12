import json
import os
from pathlib import Path
from shutil import rmtree

from styx.backend.python import to_python
from styx.frontend.boutiques import from_boutiques
from styx.ir.core import Documentation

PATH_PACKAGES = Path("packages")
PATH_DESCRIPTORS = Path("descriptors")
PATH_OUTPUT = Path("python/src/niwrap")


def iter_packages():
    for filename_package in PATH_PACKAGES.glob("*.json"):
        with open(filename_package) as filehandle_package:
            yield filename_package, json.load(filehandle_package)


def iter_descriptors(package):
    for filename_descriptor in (PATH_DESCRIPTORS / package["id"]).glob("**/*.json"):
        with open(filename_descriptor) as filehandle_descriptor:
            yield filename_descriptor, json.load(filehandle_descriptor)


# =============================================================================
# |                               COMPILE                                     |
# =============================================================================


def stream_descriptors():
    for _, package in iter_packages():
        print("*" * 80)
        print(f"COMPILING {package['name']}")
        print("*" * 80)
        for file_descriptor, descriptor in iter_descriptors(package):
            print(f"> Compiling: {file_descriptor}")
            if file_descriptor.stem != descriptor["name"]:
                print("Patching name...")
                descriptor["name"] = file_descriptor.stem

            descriptor["container-image"] = {
                "image": package["container"],
                "type": "docker"
            }
            
            package_docs = Documentation(
                title=package["name"], urls=[package["url"]]
            )
            yield from_boutiques(descriptor, package["id"], package_docs)


def compile_wrappers():
    rmtree(PATH_OUTPUT, ignore_errors=True)

    for py, module_path in to_python(stream_descriptors()):
        path_out = Path(str(PATH_OUTPUT / "/".join(module_path)) + ".py")
        path_out.parent.mkdir(parents=True, exist_ok=True)
        path_out.write_text(py, encoding="utf8")


# =============================================================================
# |                           UPDATE README                                   |
# =============================================================================


def update_readme():
    packages = sorted([package for _, package in iter_packages()], key=lambda x: x['name'])

    buf = "| Package | Status | Version | API Coverage |\n"
    buf += "| --- | --- | --- | --- |\n"


    for package in packages:
        name_link = f"[{package['name']}]({package['url']})"
        
        # calculate coverage percent
        total_endpoints = len(package['api']['endpoints'])
        done_endpoints = len([x for x in package['api']['endpoints'] if x['status'] == 'done'])
        missing_endpoints = len([x for x in package['api']['endpoints'] if x['status'] == 'missing'])
        ignored_endpoints = len([x for x in package['api']['endpoints'] if x['status'] == 'ignore'])

        assert total_endpoints == done_endpoints + missing_endpoints + ignored_endpoints

        relevant_endpoints = total_endpoints - ignored_endpoints

        coverage_percent = done_endpoints / relevant_endpoints * 100

        coverage = ""
        if missing_endpoints == 0:
            coverage = f"{done_endpoints}/{relevant_endpoints} (100% 🎉)"
        else:
            coverage = f"{done_endpoints}/{relevant_endpoints} ({coverage_percent:.1f}%)"

        container_tag = package.get('container')
        if container_tag:
            docker_image, docker_tag = package['container'].split(':')
            docker_hub = f"https://hub.docker.com/r/{docker_image}"
            container = f"[`{docker_tag}`]({docker_hub})"

        buf += f"| {name_link} | {package['status']} | {container if container_tag else '?'} | {coverage} |\n"


    # Replace text in README.md between <!-- START_PACKAGES_TABLE --> and <!-- END_PACKAGES_TABLE -->
    TOKEN_START = '<!-- START_PACKAGES_TABLE -->'
    TOKEN_END = '<!-- END_PACKAGES_TABLE -->'

    PATH_README = Path('README.md')

    with open(PATH_README, 'r') as f:
        readme = f.read()
        start = readme.find(TOKEN_START) + len(TOKEN_START)
        end = readme.find(TOKEN_END)
        assert start >= 0
        assert end >= 0
        assert start < end
        new_readme = readme[:start] + "\n\n" + buf + "\n" + readme[end:]

    with open(PATH_README, 'w', encoding="utf-8") as f:
        f.write(new_readme)
        f.write("\n")
        print("Updated README.md")


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    assert PATH_DESCRIPTORS.exists() and PATH_PACKAGES.exists()

    print("=== COMPILE WRAPPERS ===")
    compile_wrappers()

    print("=== UPDATE README ===")
    update_readme()
