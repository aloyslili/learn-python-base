import pandas as pd
def price_60_90(a):
    return  60<=a<90

def discount_60_90(a):
    return  5<=a<7

# 数据筛选

books = pd.read_excel('D:/projects/output.xlsx', index_col='ID')
books = books.loc[books['price'].apply(price_60_90)].loc[books['discount'].apply(discount_60_90)]
print(books)