# compare csv content by pandas
import pandas as pd

columns = ('id', 'name', 'age', 'address', 'phone')
index_col = ('id')

df1 = pd.read_csv('file1.csv', encoding='utf-8', names=columns, index_col=index_col)
df2 = pd.read_csv('file2.csv', encoding='utf-8', names=columns, index_col=index_col)

df1.sort_index(inplace=True)
df2.sort_index(inplace=True)

sorted_df = df1.sort_values(by=['id'], ascending=True)
print(sorted_df.head(5))

print(len(df1.index))

if len(df1.index) == len(df2.index):
    if df1.equals(df2) == False:
        # compare csv content
        df_output = df1.compare(df2, result_names=('file1', 'file2'))
        df_output.to_csv('output.csv', encoding='utf-8')
        # print(df_output.info())