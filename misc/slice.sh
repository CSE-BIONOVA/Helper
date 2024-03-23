#!/bin/bash

lines=()

while IFS= read -r line; do
    lines+=("$line")
done < genome_filenames/og_fungi.csv

echo "$lines"

for ((i=0; i<${#lines[@]}; i+=500)); do
    filename="genome_filenames/og_fungi_$((i/500)).csv"
    printf "%s\n" "${lines[@]:i:500}" > "$filename"
done
