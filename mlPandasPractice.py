import pandas as pd
# Creating series from a list using default index
a=[1,7,2]
# myvar=pd.Series(a)
# print(myvar)
# print(myvar[0])

# Creating series from a list with custom index
myVar=pd.Series(a,index=["x","y","z"])
print(myVar)
print(myVar[0])

# Creating series from a list with custom index
ages=pd.Series([22,35,58],name="Age")
print(ages)

# Creating seires with a dictionary
calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)

myvvar=pd.Series(calories,index=['day1','day2'])
print(myvvar)

# Creating dataframe with a dictonary
df=pd.DataFrame({'Name':['Ali','Aliya','Zaid'],'Age':[22,21,23],'Gender':['male','female','male']})
print(df)

# Printing only 1 column of a dataframe
print(df['Age'])

