import json
import os
import glob


if __name__ == '__main__':
    # set wd to the root of the project
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    assert os.path.exists('frameworks/fsl.json')
    assert os.path.exists('frameworks/afni.json')

    frameworks = []

    for framework_json in glob.glob('frameworks/*.json'):
        with open(framework_json, 'r') as f:
            framework = json.load(f)
        frameworks.append(framework)

    # sort by name
    frameworks = sorted(frameworks, key=lambda x: x['name'])


    buf = "| Framework | Approach | Status | API Coverage |\n"
    buf += "| --- | --- | --- | --- |\n"


    for framework in frameworks:
        name_link = f"[{framework['name']}]({framework['url']})"
        
        # calculate coverage percent
        total_endpoints = len(framework['api']['endpoints'])
        done_endpoints = len([x for x in framework['api']['endpoints'] if x['status'] == 'done'])
        missing_endpoints = len([x for x in framework['api']['endpoints'] if x['status'] == 'missing'])
        ignored_endpoints = len([x for x in framework['api']['endpoints'] if x['status'] == 'ignored'])

        assert total_endpoints == done_endpoints + missing_endpoints + ignored_endpoints

        coverage_percent = done_endpoints / (done_endpoints + missing_endpoints) * 100

        coverage = ""
        if missing_endpoints == 0:
            coverage = f"{done_endpoints}/{total_endpoints} (100% 🎉)"
        else:
            coverage = f"{done_endpoints}/{total_endpoints} ({coverage_percent:.1f}%)"

        buf += f"| {name_link} | {framework['approach']} | {framework['status']} | {coverage} |\n"


    # Replace text in README.md between <!-- START_FRAMEWORKS_TABLE --> and <!-- END_FRAMEWORKS_TABLE -->
    TOKEN_START = '<!-- START_FRAMEWORKS_TABLE -->'
    TOKEN_END = '<!-- END_FRAMEWORKS_TABLE -->'
    with open('README.md', 'r') as f:
        readme = f.read()
        start = readme.find(TOKEN_START) + len(TOKEN_START)
        end = readme.find(TOKEN_END)
        assert start >= 0
        assert end >= 0
        assert start < end
        new_readme = readme[:start] + "\n\n" + buf + "\n" + readme[end:]

    with open('README.md', 'w', encoding="utf-8") as f:
        f.write(new_readme)
        f.write("\n")
        print("Updated README.md")

    