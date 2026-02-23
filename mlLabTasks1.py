import numpy as np
import matplotlib.pyplot as plt


x=[1,2,3,4,5,6,7,8]
y=[8,7,6,5,4,3,2,1]

arr1=np.asarray(x,dtype=float)
arr2=np.asarray(y,dtype=int)
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.plot(arr1,arr2)
plt.show()
print(arr1)
print(arr2)

categories=['Apple','Banana','Cherry','Data','Mango']
values=[5,7,3,9,6]
arr3=np.asarray(values,dtype=float)
plt.pie(values,labels=categories)
plt.show()


arr5=np.asarray(x,dtype=float)
arr6=np.asarray(y,dtype=int)
plt.scatter(arr5,arr6)
plt.title("Scatter")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.show()

data=[50,20,30,40,60,10,40,45,25,35,95]
plt.title("Histogram")
plt.hist(data)
plt.show()



