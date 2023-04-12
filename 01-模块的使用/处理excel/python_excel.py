from openpyexcel import Workbook, load_workbook
# # 创建一个excel
# wb = Workbook()
# # 获取当前active的sheet
# sheet = wb.active
# # print(wb.active)
# # 修稿sheet表名
# sheet.title = "我的第一个excel"
#
# # 打开已有文件
# # wb = load_workbook("excel_text.xlsx")
#
# # 写数据
# sheet["B9"] = "哈哈哈"
#
# # 保存表单
# wb.save("excel_text.xlsx")


# 打开已有文件
wb = load_workbook("excel_text.xlsx")
# 吧sheetname名字打印出来
print(wb.sheetnames)
sheet = wb.get_sheet_by_name("Sheet1")
# 获取的是一个对象sheet["B5"]
# print(sheet["B5"].value)
# 遍历数据表
# for row in sheet:
#     print(row)
#     for cell in row:
#         print(cell.value, end=',')
#     print()

# 读取某一块数据
# for row in sheet.iter_rows(min_row=4, max_row=20, max_col=3):
#     for cell in row:
#         print(cell.value, end=',')
#     print()