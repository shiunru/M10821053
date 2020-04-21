import numpy as np
import pandas as pd
array1 = np.array([[1, 2],
                   [3, 4]])
array2 = np.array([[5, 6],
                   [7, 8]])
array11 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])
# print(array1 * array2)
# print(array1.dot(array2))
# file = 'a.npy'
# with open(file, 'wb') as f:
#     np.save(f, array11)
# with open(file, 'rb') as f:
#     array12 =np.load(f)
# print(array12)
# file1 = 'test.out'
# np.savetxt(file1, array11, delimiter=',')
#
# array13 = np.loadtxt(file1, delimiter=',')
# file = 'practice1.npy'
# with open(file, 'rb') as f:
#     array1 = np.load(f)
#
#
# array1[array1 < 0] = 0
# array1[array1 % 3 == 0] = array1[array1 % 3 == 0]/3
# print(array1)
#
# np.random.seed(123)
# array123 = np.random.randint(-10, 30, size=(10, 3))
# print(array123)
# array123 = array123.reshape(2, 15)
# print(array123)

s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s2)

data = {'a': 1, 'b': 2, 'c': 3}
s3 = pd.Series(data)
print(s3)
s4 = pd.Series(data, ['a', 'b', 'd'])
print(s4)
print(s1.values)
s2['e'] = 6
s4.index = ['Eric', 'Lisa', 'Amber']
print(s4.isnull())
print(s4.sort_index(ascending=False))
