#!/bin/bash

for ((i=0; i<25; i++))
do
    folder="fungi_${i}"
    tmux new-session -d -s "$folder"
    tmux send-keys -t "$folder" "cd home/mbadmin/Documents/Genome/Fungi" Enter
    tmux send-keys -t "$folder" "conda activate simlord" Enter
    tmux send-keys -t "$folder" "bash ../../BashScripts/Helper/generate_reads/simlord_i.sh " Enter
    tmux send-keys -t "$folder" "fungi" Enter
    tmux send-keys -t "$folder" "$i" Enter
    # tmux kill-session -t "$folder"
done