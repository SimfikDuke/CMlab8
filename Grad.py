import numpy as np


class Grad(object):
    def __init__(self, array):
        self.n = len(array)
        self.a = np.array([array[i][0:-1] for i in range(self.n)], dtype=float)
        self.b = np.array([array[i][-1] for i in range(self.n)], dtype=float)
        #self.d = np.array([self.b[i]/self.a[i][i] for i in range(self.n)], dtype=float)
        self.xk = np.array([0,0,1], dtype=float)#self.d
        self.xk1 = np.array([0,0,1], dtype=float)#self.d
        self.r = self.getR()
        self.bk = self.getBk()
        self.eps = 1e111

    def getR(self):
        r = np.dot(self.a, self.xk) - self.b
        return r

    def getBk(self):
        Bk = np.dot(self.r, self.r) / np.dot(np.dot(self.a, self.r), self.r)
        return Bk

    def print_all(self):
        print('a')
        print(self.a)
        print('b')
        print(self.b)
        print('r')
        print(self.r)
        print('Bk')
        print(self.bk)
        print('Ar')
        print(np.dot(self.a, self.r))
        print(' ')

    def print_epsilon(self, n='n'):
        print("Epsilon("+str(n)+") = ", end='')
        print(self.eps)

    def do_grad(self, n='n'):
        self.r = self.getR()
        self.bk = self.getBk()
        self.xk = self.xk - np.dot(self.bk, self.r)
        self.eps = np.linalg.norm(self.r)# * abs(self.bk)
        print("BkAr("+str(n)+") = ")
        print(np.dot(self.bk, np.dot(self.a, self.r)))
        print("Bk("+str(n)+") = ")
        print(self.bk)
        print("r("+str(n)+") = ")
        print(self.r.reshape(self.n,1))
        #print("X("+str(n)+") = ")
        #print(self.xk.reshape(self.n,1))

    def grad_spusk(self, epsilon=1e-10):
        i = 1
        while self.eps > epsilon:
            self.do_grad(i)
            self.print_epsilon(i)
            i += 1
            print(" ")
        print("Result in "+str(i)+" iteration. X = ")
        print(self.xk.reshape(self.n, 1))