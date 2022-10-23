#!/bin/bash

for FILE in output/original/; do echo $FILE ; done;

for filename in output/original/*.txt; do
    make SOURCE_FILE="$filename"
done