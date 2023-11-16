import pandas as pd
import sys

def read_csv(csv_file):
    df = pd.read_csv(csv_file, header=None)
    rows = df.shape[0]
    print(df)
    dataframe = pd.DataFrame(columns = ["pdb", "dir_name"])

    for i in range(rows):
        pdb_name = df.loc[i][1]
        pdb = pdb_name + '.pdb'
        dir_name = "relax_outputs_" + pdb_name[6:-5]

        dataframe.at[i, "pdb"] = pdb
        dataframe.at[i, "dir_name"] = dir_name
    
    with open('./dir_names.csv', 'a') as f:
        dataframe.to_csv(f, index = False, header=False)


#read_csv('../output2/IgG3_SpA_relaxed_scores.csv')
#csv file will be top600_averaged_scores.csv

def main():
    scriptname = sys.argv[0]
    csv = sys.argv[1]

    print("Script name:", scriptname)
    print("csv:", csv)
    return csv
    
if __name__ == "__main__":
    main()

csv = main()
my_result = read_csv(csv_file=csv)
