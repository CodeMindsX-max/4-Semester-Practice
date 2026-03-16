import matplotlib.pyplot as plt
x=[0,1,2,3,4,5,6,7,8,9]
y=[0,1,4,9,16,25,36,49,64,81]
plt.title("Line plot")
plt.xlabel(" X-AXIS")
plt.ylabel(" Y-AXIS")
plt.grid()
plt.plot(x,y, c='green')
plt.show()


cate=['Apple','Banana','Cherry','Date','Mango']
val=[5,7,3,8,9]
plt.bar(cate,val,color='pink')
plt.title(" BAR CHART OF DATA POINTS")
plt.xlabel(" Score")
plt.ylabel("Matches")
plt.grid()
plt.show()


sizes=[40,25,20,15]
labels=['python','java','c++','javascript']
plt.pie(sizes,labels=labels, autopct='%1.1f%%',startangle=90)
plt.title(" Pie Chart ")
plt.show()

x=[1,2,3,4,5,6]
y=[5,3,6,2,7,4]
plt.scatter(x,y,color='red')
plt.title(" Scatter plot OF DATA points")
plt.xlabel(" x-axis ")
plt.ylabel(" y-axis ")
plt.grid()
plt.show()


data=[55,65,75,80,80,85,90,95,95,100,100,100,70,75,85,90,95,60,65,70]
plt.hist(data,color='blue')
plt.title(" HISTOGRAM OF DATA")
plt.xlabel(" Value ")
plt.ylabel(" Frequencies")
plt.grid()
plt.show()