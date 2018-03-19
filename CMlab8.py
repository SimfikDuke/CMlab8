from Iter import Iter
import numpy as np

tempArr = [
    [10, 2, -1, 5],
    [-2, -6, -1, 24.42],
    [1, -3, 12, 36]
]
epsilon = 1e-5

npArr = np.array(tempArr, dtype=float)
myIter = Iter(npArr)
myIter.print_all()
myIter.simple_iterations(epsilon)
