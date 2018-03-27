import numpy as np


class Iter(object):
    def __init__(self, array):
        self.n = len(array)
        self.a = array
        self.b = np.array([array[i][-1] for i in range(self.n)], dtype=float)
        self.c = self.getC()
        self.d = np.array([self.b[i]/self.a[i][i] for i in range(self.n)], dtype=float)
        self.xn = np.array([0,0,1], dtype=float)#self.d
        self.xn1 = np.array([0,0,1], dtype=float)#self.d
        self.eps = 1e10

    def getC(self):
        c = np.zeros((self.n, self.n))
        for i in range(self.n):
            for k in range(self.n):
                if i != k:
                    c[i][k] = -self.a[i][k]/self.a[i][i]
                else:
                    c[i][k] = 0
        return c

    def print_all(self):
        print('a')
        print(self.a)
        print('b')
        print(self.b)
        print('c')
        print(self.c)
        print('d')
        print(self.d)
        print(' ')

    def print_epsilon(self, n='n'):
        print("Epsilon("+str(n)+") = ", end='')
        print(self.eps)

    def do_simple_iter(self, n='n'):
        self.xn = self.xn1
        self.xn1 = np.dot(self.c, self.xn) + self.d
        #self.eps = max(abs(self.xn1 - self.xn))
        self.eps = np.linalg.norm(self.xn1-self.xn)
        print("X("+str(n)+") = ")
        print(self.xn1.reshape(3,1))

    def simple_iterations(self, epsilon=1e-10):
        i = 1
        while self.eps > epsilon:
            self.do_simple_iter(i)
            self.print_epsilon(i)
            i += 1
            print(" ")