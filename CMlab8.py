from Iter import Iter
import numpy as np

tempArr = [
    [10, 2, -1, 5],
    [-2, -6, -1, 24.42],
    [1, -3, 12, 36]
]
npArr = np.array(tempArr, dtype=float)
myIter = Iter(npArr)
print('a')
print(myIter.a)
print('b')
print(myIter.b)
print('c')
print(myIter.c)
print('d')
print(myIter.d)
print(' ')

for i in range(10):
    myIter.do_simple_iter(i+1)
    myIter.print_epsilon(i+1)
    print(" ")