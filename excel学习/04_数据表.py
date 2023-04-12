import pandas as pd
import matplotlib.pyplot as plt
books = pd.read_excel('D:/projects/output.xlsx')
print(books)
books.plot.bar(x='name', y='price')
plt.show()

