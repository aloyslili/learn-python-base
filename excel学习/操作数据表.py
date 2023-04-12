import pandas as pd
# from openpyexcel import Workbook, load_workbook
# 去掉空行和空列
books = pd.read_excel('D:/projects/output.xlsx', skiprows=3, usecols="C:F")
# wb = load_workbook("D:/projects/output.xlsx")
# books=pd.read_excel('D:/projects/output.xlsx',sheet_name=None)
# print(list(books.keys()))
# for j in books.keys():
#     print(j)
print(books)
# sheet = wb.get_sheet_by_name("Sheet2")
# print(wb.sheetnames)
# sheet = wb.get_sheet_by_name("Sheet2")
# print(sheet)
# 区域填充数据