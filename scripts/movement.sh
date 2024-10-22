#!/bin/bash

device=$1

if [ $# -ne 2 ]; then
    echo "Incorrect usage: ./movement.sh <device>"
    exit 1
fi 

if [ "$device" = "desk" ]; then 
    cd /mnt/c/Users/kaliy/wargames/something-awesome
elif [ "$device" = "lap" ]; then
    echo "Waiting..."
else 
    echo "What?"
fi