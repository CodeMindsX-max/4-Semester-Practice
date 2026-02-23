import matplotlib.pyplot as plt

carName=['BMW','Audi','Tesla','Bugati','Supra','Merceds','FX','Mehran']
carPrice=[20000000,15000000,10000000,60000000,20000000,70000000,1000000,2000000]
carMunfuc=['German','German','USA','France','Japan','German','Japan','Pakistan']


plt.bar(carName,carPrice)
plt.title('Bar Chart Plot')
plt.xlabel("Car Names")
plt.ylabel("Car Prices")
plt.grid()
plt.show()

plt.title("Line Chart Plot")
plt.xlabel("Car Names")
plt.ylabel("Car Prices")
plt.grid()
plt.plot(carName,carPrice,color='red')
plt.show()

plt.hist(carPrice,color='green')
plt.title("Histogram Char Plot")
plt.xlabel("Car Names")
plt.ylabel("Car Prices")
plt.grid()
plt.show()

plt.scatter(carName,carPrice,color='brown')
plt.title("Scatter Chart Plot")
plt.xlabel("Car Names")
plt.ylabel("Car Prices")
plt.grid()
plt.show()

plt.pie(carPrice,labels=carName,autopct='%1.1f%%',startangle=90)
plt.title("Pie Chart Plot")
plt.show()