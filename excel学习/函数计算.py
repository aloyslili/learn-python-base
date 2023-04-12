import pandas as pd
# 读取数据表 D:/projects/output.xlsx索引
books = pd.read_excel('D:/projects/output.xlsx', index_col='ID')
books['priceall'] = books["price"]*books["discount"]
print(books)