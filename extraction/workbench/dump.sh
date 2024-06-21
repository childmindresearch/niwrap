#!/bin/bash

# Run this script from source/workbench/build after cmake and make

mkdir -p outs

# Loop through each subcommand in subcommands.txt
while IFS= read -r subcommand; do
    echo "Executing wb_command $subcommand"
    # Execute wb_command with the current subcommand and write output to a file
    source/build/CommandLine/wb_command "$subcommand" > "outs/${subcommand}_output.txt" 2> "outs/${subcommand}_error.txt"
done < out_commands.txt