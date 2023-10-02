"""
This module compares two CSV files using pandas.
"""

import pandas as pd

# Define constants
COLUMNS = ['id', 'name', 'age', 'address', 'phone']
INDEX_COL = 'id'

def main():
    """Main function to compare two CSV files."""
    df1 = pd.read_csv('file1.csv', encoding='utf-8', names=COLUMNS, index_col=INDEX_COL)
    df2 = pd.read_csv('file2.csv', encoding='utf-8', names=COLUMNS, index_col=INDEX_COL)

    df1.sort_index(inplace=True)
    df2.sort_index(inplace=True)

    sorted_df = df1.sort_values(by=['id'], ascending=True)
    print(sorted_df.head(5))

    print(len(df1.index))

    if len(df1.index) == len(df2.index):
        if not df1.equals(df2):
            # Compare CSV content
            df_output = df1.compare(df2, result_names=('file1', 'file2'))
            df_output.to_csv('output.csv', encoding='utf-8')

if __name__ == "__main__":
    main()
