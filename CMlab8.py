from Iter import Iter
import numpy as np

tempArr = [
    [10, 2, -1, 5],
    [-2, -6, -1, 24.42],
    [1, -3, 12, 36]
]

npArr = np.array(tempArr, dtype=float)
myIter = Iter(npArr)
myIter.print_all()

for i in range(10):
    myIter.do_simple_iter(i+1)
    myIter.print_epsilon(i+1)
    print(" ")