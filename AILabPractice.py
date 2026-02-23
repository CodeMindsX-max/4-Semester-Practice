# # a=(2,4,6,8)
# # b=[]
# # for x in a:
# #     b.append(x)

# # b.remove(4)
# # b.insert(4,10)
# # b.insert(2,7)
# # c=()
# # for x in b:
# #     c=a+tuple(x)
# # print(b)
# # print(c)

# a=(2,4,6,8)
# b=list(a)

# b.remove(4)
# b.insert(3,10)
# b.insert(2,7)
# b.append(20)
# print(b)
# b[3]=5

# c=tuple(b)

# print(c)

# d,e,f,*g=a

# print(g)

# std={'name':['Ahmed','Ali','Asim'],'age':[21,20,22],'english':[50,45,49],'urdu':[48,55,56],'ai':[43,45,54]}
# average=[]
# sum=std['english'][0]+std['urdu'][0]+std['ai'][0]
# average.append(sum/3)
# sum=std['english'][1]+std['urdu'][1]+std['ai'][1]
# average.append(sum/3)
# sum=std['english'][2]+std['urdu'][2]+std['ai'][2]
# average.append(sum/3)

# print(max(average))


# prices = [100, 250, 80, 400]

# prices_with_tax = list(map(lambda p: p * 1.18, prices))
# print(prices_with_tax)


import pandas as pd

data=pd.read_csv(r"D:\Python Programs\4 Semester Practice\myDetail.csv")
print(data.head())
data=data.drop(['name'], axis=1)
print(data.head())