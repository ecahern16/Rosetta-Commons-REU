#!/bin/sh
module load "Rosetta"

ROSETTA="/software/all/Rosetta/3.13-gompi-2020b"

cd ./$1
mkdir rmsd_outputs

$ROSETTA/bin/rosetta_scripts.mpi.linuxgccrelease \
-in:file:l path.list -in:file:native $2 \
-parser:protocol ../rmsd.xml -out:path:pdb ./rmsd_outputs

cat score.sc | awk '{print $23 "," $21 "," $2}' | awk '(NR>1)' | awk 'NR == 1; NR > 1 {print $0 | "sort"}' > rmsd_script.csv

cd ../

#path.list has path to all pdb files you want rmsd of 
