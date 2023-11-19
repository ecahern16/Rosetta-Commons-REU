#!/bin/sh

module load "Rosetta"
module load Anaconda3
source /software/all/Anaconda3/2021.11/etc/profile.d/conda.sh
conda activate fasta

ROSETTA="/software/all/Rosetta/3.13-gompi-2020b"

echo $1
mkdir -p relax_outputs_${1%.*}
cp post_relax.py ./relax_outputs_${1%.*}

$ROSETTA/bin/relax.mpi.linuxgccrelease \
-s $1 -linmem_ig 100 -use_input_sc -nstruct 6 -relax:constrain_relax_to_start_coords \
-relax:fast -out:path:all ./relax_outputs_${1%.*} -out:prefix relax_

cd relax_outputs_${1%.*}
cat relax_score.sc | awk '{print $2 "," $22}' | awk '(NR>1)' | awk 'NR == 1; NR > 1 {print $0 | "sort -n"}' > total_scores.csv

python post_relax.py total_scores.csv

cd ../

