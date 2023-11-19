import pandas as pd
import sys

def read_csv(csv_file):
    df = pd.read_csv(csv_file, header=None)
    rows = df.shape[0]
    print(df)
    
    best_i_sc = df.loc[1][1]
    pdb_name = df.loc[1][3]
    st_rmsd = df.loc[1][0]
    fnat = df.loc[1][2]
    
    for i in range(1,int((rows*0.5)+1)):
        if df.loc[i][1] > best_i_sc:
            best_i_sc = df.loc[i][1]
            pdb_name = df.loc[i][3]
            st_rmsd = df.loc[i][0]
            fnat = df.loc[i][2]

        print(i)
        print(best_i_sc)
    
    return best_i_sc, pdb_name, st_rmsd, fnat

def add_to_csv(best_i_sc, pdb_name, st_rmsd, fnat):
    pdb = pdb_name + '.pdb'
    dir_name = 'docking_outputs' + pdb_name[5:-5]
    
    dataframe = pd.DataFrame(columns = ["pdb", "dir_name", "st_rmsd", "I_sc", "Fnat"])
    dataframe.at[0, "pdb"] = pdb
    dataframe.at[0, "dir_name"] = dir_name
    dataframe.at[0, "st_rmsd"] = st_rmsd
    dataframe.at[0, "I_sc"] = best_i_sc
    dataframe.at[0, "Fnat"] = fnat
    print(dataframe)

    with open('../dock_dir_names.csv', 'a') as f:
        dataframe.to_csv(f, index = False, header='pdb,dir_name,st_rmsd,I_sc,Fnat')

#read_csv('./docking_values.csv')

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
add_to_csv(my_result[0], my_result[1], my_result[2], my_result[3])
