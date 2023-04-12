import pandas as pd
import matplotlib.pyplot as plt
people = pd.read_excel('D:/projects/output.xlsx',index_col='From')
people['price'].plot.pie()
plt.show()