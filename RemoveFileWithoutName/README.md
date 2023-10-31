Sure, here's a README.md file for your script:

# File Deletion Script

This is a bash script that allows you to delete files in a directory based on their extension and a specific word in their filename.

## Functionality

The script works as follows:

1. It prompts the user to enter the directory path.
2. It then asks for the file extension to look for.
3. Finally, it asks for a word to search in the file names.

The script navigates to the specified directory and finds all files with the given extension. If a file's name does not contain the specified word, the script deletes that file.

## Usage

To use this script, you need to have bash installed on your system. You can run the script using the following command:

```bash
./file_deletion_script.sh
```

Before running the script, you need to give it executable permissions. You can do this with the following command:

```bash
chmod +x file_deletion_script.sh
```

## Caution

Please be careful while using this script as it deletes files. Make sure to double-check the directory path, file extension, and word before running the script.
