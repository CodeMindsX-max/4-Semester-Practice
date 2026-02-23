import numpy as np
l1=[2,4,6,8]

# arr=np.array(l1,dtype=float)
# arr=np.asarray(l1,dtype=np.uint32)

arr=np.asarray(l1,dtype=np.int32)
arr1=np.arange(10,20,2)
arr2=np.zeros((3,3))
arr3=np.ones((3,3))
arr3[1][1]=22

print(arr3)
print(arr2)
print(arr1)
print((arr1[:4]))


print(l1)
print(arr)
arr[0]+=3
print(arr)

arr+=1
print(arr)

