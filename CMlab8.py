from Iter import Iter
from Grad import Grad
import numpy as np

epsilon = 1e-3

def iter():
    tempArr = [
        [6, 3, 2, 4],
        [4, 7, 1, 7],
        [5, 2, 9, 2]
    ]

    npArr = np.array(tempArr, dtype=float)
    myIter = Iter(npArr)
    myIter.print_all()
    myIter.simple_iterations(epsilon)

def grad():
    arr = [
        [6, 3, 2, 4],
        [4, 7, 1, 7],
        [5, 2, 9, 2]
    ]
    gr = Grad(np.array(arr, dtype=float))
    gr.print_all()
    gr.grad_spusk(epsilon)


grad()