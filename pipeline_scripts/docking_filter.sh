#!/bin/bash

cd docking_outputs_${1%.*}
cat docking.fasc | awk '{print $28 "," $6 "," $5 "," $30}' | awk '(NR>1)' | awk 'NR == 1; NR > 1 {print $0 | "sort -n"}' > docking_values.csv

cp ../filter_docking_results.py .
python filter_docking_results.py docking_values.csv

cd ../
