#!/bin/bash

for i in *.pdb;do echo /home/sc.uni-leipzig.de/jy302xazi/erin/protein_generator/run_1/paula_output/pdb/relax.sh $i >> relax.array;done

head relax.array -n 3021 >> first_half_relax.array

tail relax.array -n 3022 >> second_half_relax.array
