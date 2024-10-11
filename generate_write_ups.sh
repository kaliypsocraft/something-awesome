#!/bin/bash

traverse_directory() {
    for entry in "$1"/*; do
        if [ -d "$entry" ]; then
            dir_name="$(basename "$entry")"  
            echo "$dir_name"  
        
            touch "$entry/$dir_name.md"
        fi
    done
}

# traverse current directory
traverse_directory "."
