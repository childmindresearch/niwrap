import pathlib
from collections import defaultdict
import json

def load_descriptors():
    """Yield (file_path, json_data) from descriptor files."""
    for file_path in pathlib.Path("descriptors").glob("*/*.json"):
        with open(file_path, 'r', encoding='utf-8') as f:
            yield file_path, json.load(f)

def check_command_line():
    suspicious_chars = [
        "  ",  # double space
        *"<>|&%/\\´`#'+~@\"-\t\n=:.,;(){}§€$?!^°",
    ]

    stats = defaultdict(int)
    package_stats = defaultdict(int)

    for file_path, data in load_descriptors():
        package = file_path.parent.name
        command_line = data.get('command-line')
        name = data.get('name', '')

        # Check for missing command line
        if not isinstance(command_line, str):
            print(f"Command-line missing in {file_path}")
            stats["missing"] += 1
            print("-" * 80)
            continue

        # Clean command line
        command_line_clean = command_line.removeprefix("wb_command -").removeprefix(name)

        # Check for suspicious characters
        for sus in suspicious_chars:
            if sus in command_line_clean:
                print(f"Suspicious string '{sus}' in {file_path}")
                print(f"Original: '{command_line}'")
                print("-" * 80)
                
                stats[f"suspicious '{sus}'"] += 1
                stats["suspicious total"] += 1
                package_stats[package] += 1
                break

    # Print statistics
    print("\nOverall Statistics:")
    print("-" * 20)
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\nSuspicious Commands by Package:")
    print("-" * 20)
    for package, count in package_stats.items():
        print(f"{package}: {count}")

if __name__ == "__main__":
    check_command_line()
