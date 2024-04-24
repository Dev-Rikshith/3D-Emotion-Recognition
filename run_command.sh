#!/bin/bash

directory="/path/to/your/project"

log_file="script_log.txt"

commands=(
   "python Project1.py RF o datafolder"
    "python Project1.py RF t datafolder"
    "python Project1.py RF x datafolder"
    "python Project1.py RF y datafolder"
    "python Project1.py RF z datafolder"
    "python Project1.py SVM o datafolder"
    "python Project1.py SVM t datafolder"
    "python Project1.py SVM x datafolder"
    "python Project1.py SVM y datafolder"
    "python Project1.py SVM z datafolder"
    "python Project1.py TREE o datafolder"
    "python Project1.py TREE t datafolder"
    "python Project1.py TREE x datafolder"
    "python Project1.py TREE y datafolder"
    "python Project1.py TREE z datafolder"

)

for file in "$directory"/*.py; do
    echo "Processing file: $file" >> "$log_file"
    
    for cmd in "${commands[@]}"; do
        echo "Running command: $cmd" >> "$log_file"
        echo "" >> "$log_file" 
        eval "$cmd" >> "$log_file" 2>&1  
        echo "" >> "$log_file"  
    done

    echo "" >> "$log_file"  
done

echo "All files processed. Log saved to $log_file"
