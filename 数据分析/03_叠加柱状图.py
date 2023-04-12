import pandas as pd
import matplotlib.pyplot as plt
people = pd.read_excel('D:/projects/output.xlsx')
# 分组 排序
# people.sort_values(by='price', inplace=True,ascending=False)
print(people)
people.plot.bar(x='name',y=['price','nowprice','oldprice'],stacked=True,title="User Behavior")
plt.tight_layout()
# plt.title("hh", fontsize="16")
# 显示图片
plt.show()