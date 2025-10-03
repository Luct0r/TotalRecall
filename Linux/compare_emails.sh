#!/bin/bash
##
### Checks two files for duplicate emails and displays the results
#

# Check if two files are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <fileA> <fileB>"
    exit 1
fi

fileA=$1
fileB=$2

# Check if files exist
if [ ! -f "$fileA" ]; then
    echo "Error: $fileA not found"
    exit 1
fi

if [ ! -f "$fileB" ]; then
    echo "Error: $fileB not found"
    exit 1
fi

echo "=== Emails only in $fileA ==="
comm -23 <(sort "$fileA") <(sort "$fileB")

echo -e "\n=== Emails only in $fileB ==="
comm -13 <(sort "$fileA") <(sort "$fileB")

echo -e "\n=== Emails in both files ==="
comm -12 <(sort "$fileA") <(sort "$fileB")
