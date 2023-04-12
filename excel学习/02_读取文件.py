import pandas as pd
people = pd.read_excel('D:/projects/output.xlsx')
# 读取行和列
# print(people.shape)
# 读取列
print(people.columns)
print(people.head(3))
print(people.tail(2))
# 表头名 不要设置表头 header = none 读取文件的时候
print(people.columns)