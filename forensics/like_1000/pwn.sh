#!/bin/bash

counter=1000
while [ "$counter" -ge 1 ]
do
    tar -xvf $counter.tar
    prev_counter=$counter
    ((counter--))
    rm -rf $prev_counter.tar
done

