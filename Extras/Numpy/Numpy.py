import numpy as np

# Array Object in Numpy is Called ndarray
# It is a data type that can hold any kind of data.
# array() is used to create ndarray object.
array = np.array([1,2,3,5,5])
print("Elements of Array are : ",array)
print("Type of Array is : ",array.dtype)
print("Type of Object is :", type(array))
print("Numpy Version is : ",np.__version__)

# we can pass list, tuple or any array like object to array
#  of lists
listsArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(listsArray)

# 0-D Array (Scalar)
# Each value is an array is a 0-D array
zerodarray=np.array(42)
print("O-D array is : ",zerodarray)

# 1-D Array (O-D arrays as its elements)
oned_array = np.array([3,5,28,2,1,3,2])
print("1-D array is : ",oned_array)

# 2-D Array (1-D arrays as its element)
# used to represent matrix or 2d order tensor
# Numpy has a whole sub module dedicated towards matrix operations called numpy.mat
twod_array = np.array([ [1,2,3],[2,4,5]])
print("2-D array is : \n",twod_array)

# Checking dimension of the array
print("Dimension of above arrays : ")
print(zerodarray.ndim)
print(oned_array.ndim)
print(twod_array.ndim)

# Creating Higher Dimension Arrays
# can define the number of dimensions by using the ndim keyword argument
nth_dim_array = np.array([[1,2,3],[4,5,6]], ndmin=5)
print("n-D array is : \n",nth_dim_array)
print("Dimension is : ",nth_dim_array.ndim)







