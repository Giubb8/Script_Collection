#!/bin/bash

# Ask the user for the directory
echo "Enter the directory path:"
read directory

# Ask the user for the file extension
echo "Enter the file extension:"
read extension

# Ask the user for the word to search in the file name
echo "Enter the word to search in the file name:"
read word

# Navigate to the desired directory
cd $directory

# Find all files with the specified extension
for file in *.$extension
do
    # Check if the file name contains the specified word
    if [[ $file != *"$word"* ]]; then
        # If it does not contain the word, delete the file
        rm "$file"
    fi
done
