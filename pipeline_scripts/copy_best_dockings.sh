#!/bin/bash

cat dock_dir_names.csv | awk '(NR>1)' | while IFS=, read -r field1 field2 field3 field4 field5
do
    PDB="$field1"
    DIR_NAME="$field2"
    echo "PDB=$PDB"
    echo "DIR_NAME=$DIR_NAME"

    cd $DIR_NAME
    cp $PDB ../best_dockings/
    echo "copied"
    cd ../
done
