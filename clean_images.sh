#!/bin/bash

for challenge in *; do
    if [ -d "$challenge" ]; then
        for exercise in "$challenge"/*; do 
            if [ -d "$exercise" ]; then 
                if [ ! -d "$exercise/images" ]; then 
                    mkdir "$exercise/images"
                fi

                mv "$exercise"/*.png "$exercise/images/" 2>/dev/null
                name=$(basename "$exercise")
                md_file="$exercise/$name.md"
                md_file="$exercise/$(basename "$exercise").md"

                if [ -f "$md_file" ]; then
                    tmp_file="$md_file.tmp"
                    > "$tmp_file"
                    while IFS= read -r line; do
                        # Used ChatGPT to obtain the Regex
                        if [[ $line =~ \!\[.*\]\(image-([0-9]+)\.png\) ]]; then
                            # Obtain the capture group
                            image_number="${BASH_REMATCH[1]}"
                            image_name="image-$image_number.png"
                            new_image_path="images/$image_name"

                            mv "$exercise/$image_name" "$exercise/$new_image_path" 2>/dev/null

    
                            line="${line//\(image-$image_number.png\)/\($new_image_path\)}"
                
                        elif [[ $line =~ \!\[.*\]\(image\.png\) ]]; then
                            new_image_path="images/image.png"
                            mv "$exercise/image.png" "$exercise/$new_image_path" 2>/dev/null

                            
                            line="${line//\(image.png\)/\($new_image_path\)}"
                        fi

                
                        echo "$line" >> "$tmp_file"
                    done < "$md_file"
                    mv "$tmp_file" "$md_file"
                fi
            fi
        done
    fi
done


