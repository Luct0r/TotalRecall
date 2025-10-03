#!/bin/bash
###
## Script to quickly search and print additional details about an email from XLSX files
##
### Requires:
# pip3 install xlsxgrep
#
### Essentially automates the following:
##
# user="email@domain.com"
# xlsxgrep "$user" -H -N --sep=";" -r .
#

# Check if file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# Check if file exists
if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found!"
    exit 1
fi

# Read file line by line and run xlsxgrep
while IFS= read -r user; do
    # Skip empty lines
    if [ -n "$user" ]; then
        echo "Searching for: $user"
        xlsxgrep "$user" -H -N --sep=";" -r .
    fi
done < "$1"
