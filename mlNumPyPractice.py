import numpy as np

a1=np.array([[2,6],[3,9]])
print(a1)
# make 2d array of 2 sub arrays

a2=np.asarray(11)
print(a2)
# print value as it is

l2=[45,134,300]
a3=np.asarray(l2,dtype=np.int8)
print(a3)
# int8 check the ranges from -128 to 127 or if no. exceed from this range then it will show out of bound

l3=[45,30,-10]
a4=np.asarray(l3,dtype=np.uint32)
print(a4)
# neglect negative values and allow all positive numbers in to the range of 0 to 2^32-1 and use all 32 to bit to store numbers
# uint means unassigned integer

a5=np.asarray(l3,dtype=np.int32)
print(a5)
# allow both negative and positive values in the range of -2^31 to 2^31-1 and use all 32 bit to store numbers

a6=np.asarray(l3,dtype=np.float)
print(a6)

a7=np.arange(10)
print(a7)

a8=np.arange(5,20,2)
print(a8)

a9=np.arange(3,28,3,dtype=float)
print(a9)

a10=np.zeros((5,8))
print(a10)

a11=np.ones((3,7))
print(a11)

a12=np.array([3,1,7,8,9,10,11,56,7,2,4])
a13=a12[:6]
a13=a13+1
print(a12)
print(a13)

