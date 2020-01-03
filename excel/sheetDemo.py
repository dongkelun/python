# python 读取多Sheet页Excel文件示例

import pandas as pd

file1 = pd.ExcelFile('../data/test.xlsx')
file2 = pd.read_excel('../data/test.xlsx')
print(file1)
print('-----------------分割线---------------------')
print(file2)

print('-----------------分割线---------------------')
file = pd.ExcelFile('D:\\data\\py\\test.xlsx')
print(file.sheet_names)

for name in file.sheet_names:
    _df = pd.read_excel(file, name)
    print(_df)

df_list = []
for name in file.sheet_names:
    _df = pd.read_excel(file, name)
    _df['班级'] = name
    df_list.append(_df)
df = pd.concat([_df for _df in df_list], sort=False)
print(df)

df: pd.DataFrame = pd.concat([_df for _df in df_list], ignore_index=True, sort=False)
print(df)

df = df.rename(columns={'姓名': 'name', '年龄': 'age', '性别': 'sex', '住址': 'address', '班级': 'class'})
print(df)

df.to_csv('../data/sheet合并.csv', index=False)
df.to_excel('../data/sheet合并.xls', index=True)
