#!/bin/bash

challenge=$1
name=$2

if [ $# -lt 2 ]; then
    echo "Incorrect usage: bash generate_challenge_file.sh <challenge_type> <name>"
    exit 1
elif [ ! -d $challenge ]; then
    echo "Incorrect challenge name"
    exit 1
fi

mkdir "$challenge/$name"

echo "Created $challenge/$name"

cp WRITE_UP_TEMPLATE.md $challenge/$name/$name.md

echo "Created $challenge/$name.md"
