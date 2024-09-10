import json
from pathlib import Path
from shutil import rmtree

from styx.backend.python import to_python
from styx.frontend.boutiques import from_boutiques
from styx.ir.core import Documentation

PATH_FRAMEWORKS = Path("frameworks")
PATH_DESCRIPTORS = Path("descriptors")
PATH_OUTPUT = Path("python/src/niwrap")


def iter_frameworks():
    for filename_framework in PATH_FRAMEWORKS.glob("*.json"):
        with open(filename_framework) as filehandle_framework:
            yield filename_framework, json.load(filehandle_framework)


def iter_descriptors(framework):
    for filename_descriptor in (PATH_DESCRIPTORS / framework["id"]).glob("**/*.json"):
        with open(filename_descriptor) as filehandle_descriptor:
            yield filename_descriptor, json.load(filehandle_descriptor)


def stream_descriptors():
    for _, framework in iter_frameworks():
        print("*" * 80)
        print(f"COMPILING {framework['name']}")
        print("*" * 80)
        for file_descriptor, descriptor in iter_descriptors(framework):
            print(f"> Compiling: {file_descriptor}")
            if file_descriptor.stem != descriptor["name"]:
                print("Patching name...")
                descriptor["name"] = file_descriptor.stem
            framework_docs = Documentation(
                title=framework["name"], urls=[framework["url"]]
            )
            yield from_boutiques(descriptor, framework["id"], framework_docs)


if __name__ == "__main__":
    rmtree(PATH_OUTPUT, ignore_errors=True)

    for py, module_path in to_python(stream_descriptors()):
        path_out = Path(str(PATH_OUTPUT / "/".join(module_path)) + ".py")
        path_out.parent.mkdir(parents=True, exist_ok=True)
        path_out.write_text(py, encoding="utf8")
