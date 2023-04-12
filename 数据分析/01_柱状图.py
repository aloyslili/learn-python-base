# import pandas as pd
# import matplotlib.pyplot as plt
# books = pd.read_excel('D:/projects/output.xlsx')
# print(books)
# books.plot.bar(x='name', y='price')
# plt.show()

#导入需要用到的模块
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'simhei'

#读取目标表格文件，并用people代表读取到的表格数据
people = pd.read_excel('D:/projects/output.xlsx')
#在控制台中输出表格数据
print(people)
#x轴是姓名，y轴是年龄
people.plot.bar(x='name',y='price',title="myfirstzhuzhuangtu")
# 紧凑型布局
plt.tight_layout()
plt.show()
