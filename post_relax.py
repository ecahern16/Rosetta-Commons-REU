from Bio import PDB
from Bio.PDB.PDBParser import PDBParser 
from Bio.PDB.Polypeptide import three_to_one 
import argparse
import pandas as pd
import sys
import csv
from csv import writer

#Getting best scoring relaxed pdb structure 
def get_csv(csv_file):
    df = pd.read_csv(csv_file)

    best_score = df.loc[0]['total_score']

    best_pdb_name = df.loc[0]['description']

    best_pdb = best_pdb_name + '.pdb'
    
    #print(df)
    #print("Best score:", best_score)
    #print(best_pdb_name)
    #print(best_pdb)

    return best_score, best_pdb_name, best_pdb


#Getting the sequence length from pdb file
def get_seq_length(pdb):
    parser = PDBParser() 
    
    structure = parser.get_structure("pdb_name", pdb)

    sequence = []
    model = structure[0]
    chain = model['A']

    for residue in chain.get_residues():
        sequence.append(three_to_one(residue.get_resname()))

    seq_len = len(sequence)
    print("Sequence length:", seq_len)
    return seq_len


#Dividing the total_score value by the sequence length & adding it to existing csv file
def divide_score(best_score, seq_len, best_pdb_name): 
    score_divided_len = best_score / seq_len
    
    dataframe = pd.DataFrame(columns = ["score/length", "best_score", "seq_len", "pdb_name"])
    dataframe.at[0, "score/length"] = score_divided_len
    dataframe.at[0, "best_score"] = best_score
    dataframe.at[0, "seq_len"] = seq_len
    dataframe.at[0, "pdb_name"] = best_pdb_name
 
    
    print("Score divided by length:", score_divided_len)
    print(dataframe)
    
    with open('../relaxed_data.csv', 'a') as f:
        dataframe.to_csv(f, index = False, header=False)


def main():
    scriptname = sys.argv[0]
    csv = sys.argv[1]

    #print("Script name:", scriptname)
    #print("csv:", csv)
    return csv

if __name__ == "__main__":
    main()

csv = main()
my_result = get_csv(csv_file=csv)
seq_len_value = get_seq_length(my_result[2])
divide_score(my_result[0], seq_len_value, my_result[1])
