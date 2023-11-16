sort -n -k1 averaged_scores.csv | head -n 600 > top600_averaged_scores.csv

python sort_for_docking.py top600_averaged_scores.csv


cat dir_names.csv | while IFS=, read -r field1 field2
do
    PDB="$field1"
    DIR_NAME="$field2"
    echo "PDB=$PDB"
    echo "DIR_NAME=$DIR_NAME"
    
    cd $DIR_NAME
    cp $PDB ../best_designs/
    echo "copied"
    cd ../
done

