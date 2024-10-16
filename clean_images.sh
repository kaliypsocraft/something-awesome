#!/bin/bash

for challenge in *; do
    if [ -d "$challenge" ]; then
        echo "Challenge: $challenge"
       for exercise in "$challenge"/*; do 
            if [ -d "$exercise" ]; then 
                echo "Exercise: $exercise"
                if [ ! -d "$exercise/images" ]; then 
                    mkdir "$exercise/images"
                fi
                mv "$exercise"/*.png "$exercise/images/" 2>/dev/null

            fi
        done
    fi
done

