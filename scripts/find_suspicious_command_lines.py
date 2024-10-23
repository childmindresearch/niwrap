import pathlib
import json

def iter_descriptors():
    for file_path in pathlib.Path("descriptors").glob("*/*.json"):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        yield file_path, data

def check_command_line():

    stats = {}
    for file_path, data in iter_descriptors():
        command_line_original = command_line = data.get('command-line', None)
        name = data.get('name', '')
        if command_line is None or not isinstance(command_line, str):
            print(f"command-line missing in \"{file_path}\"")
            stats[f"missing"] = stats.get(f"missing", 0) + 1
            print("-"*80)
            continue

        command_line: str
        command_line = command_line.removeprefix("wb_command -")
        command_line = command_line.removeprefix(name)

        suspicious_strings = [
            "  ",
            *"<>|&%/\\´`#'+~@\"-\t\n=:.,;(){}§€$?!^°",
        ]

        for sus in suspicious_strings:
            if sus in command_line:
                print(f"suspicious string \"{sus}\" in \"{file_path}\"")
                print(f" \"{command_line_original}\"")
                print("-"*80)
                stats[f"suspicious total"] = stats.get(f"suspicious total", 0) + 1
                stats[f"suspicious \"{sus}\""] = stats.get(f"suspicious \"{sus}\"", 0) + 1
                break
        
    for key, value in stats.items():
        print(key, value)

check_command_line()
