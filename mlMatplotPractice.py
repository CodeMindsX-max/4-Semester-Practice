import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# plt.title("Line Plot")
# plt.xlabel("X-AXIS")
# plt.ylabel("Y-AXIS")
# plt.grid()
# plt.plot(x,y, c='green')
# plt.show()

x=[5,2,9,4,7]
y=[10,5,8,4,2]
plt.bar(x,y, color='red')
plt.title("Bar Chart of data")
plt.xlabel("Score")
plt.ylabel("Matches")
plt.show()

plt.plot(x,y)
plt.title("Line char of data")
plt.grid()
plt.xlabel("Score")
plt.ylabel("Matches")
plt.show()

plt.hist(y, color='yellow')
plt.title("Histogram of data")
plt.xlabel("Values")
plt.ylabel("Frequenies")
plt.grid()
plt.show()

plt.scatter(x,y)
plt.title("Scatter plt data points")
plt.xlabel("Values")
plt.ylabel("Targets")
plt.grid()
plt.show()

name=['Ali','Ahmed','Akram']
marks=[80,92,57]

plt.pie(marks,labels=name,autopct='%1.1f%%',startangle=90)
plt.xlabel('Marks')
plt.ylabel('Names')
plt.title('Pie chart')
plt.show()




