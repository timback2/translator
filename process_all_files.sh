#!/bin/bash

for filename in output/original/*.txt; do
    make SOURCE_FILE="$filename"
done