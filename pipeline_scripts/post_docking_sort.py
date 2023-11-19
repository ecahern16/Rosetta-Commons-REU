import pandas as pd
import sys

def read_csv(csv_file):
    df = pd.read_csv(csv_file)
    print("Unsorted dataframe: \n", df)

    #sort by interface score
    sorted_df = df.sort_values(by = 'I_sc')
    print("\n Sorted by i_sc dataframe: \n", sorted_df)
    top_i_sc = sorted_df.iloc[1:58]
    print("\n Top 10% i_sc dataframe: \n", top_i_sc)

    #sort by Fnat
    sorted_top_i_sc = top_i_sc.sort_values(by = 'Fnat', ascending = False)
    print("\n Sorted by Fnat dataframe: \n", sorted_top_i_sc)
    top_fnat = sorted_top_i_sc.iloc[0:6]
    print("\n Top 10% Fnat dataframe: \n", top_fnat)

    with open('./top_paula_output_designs.csv', 'a') as f:
        sorted_top_i_sc.to_csv(f, index = False, header='pdb,dir_name,st_rmsd,I_sc,Fnat')


read_csv('./best_docking_designs.csv')

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

