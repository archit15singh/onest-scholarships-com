#!/bin/bash

MAIN_DIR=$(pwd)

DIRECTORIES=("bap-client-ps" "bap-network-ps" "bpp-client-ps" "bpp-network-ps")

for dir in "${DIRECTORIES[@]}"; do
    if [ -d "$dir" ]; then
        echo "Navigating to $dir and running npm install..."
        cd "$dir"
        npm install
        cd "$MAIN_DIR"
    else
        echo "Directory $dir does not exist."
    fi
done

echo "npm install completed in all directories."
