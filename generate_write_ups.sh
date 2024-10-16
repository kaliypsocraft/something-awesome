#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Incorrect usage: bash generate_write_ups.sh <directory>"
    exit 1
fi

traverse_directory() {
    for entry in "$1"/*; do
        if [ -d "$entry" ]; then
            dir_name="$(basename "$entry")"  
            echo "$dir_name"  
            
            mkdir "$entry/$dir_name.md"
        fi
    done
}

# traverse current directory
traverse_directory "$1"
