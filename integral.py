from itertools import cycle, chain
from functools import reduce
from polynomial import Polynomial


class Integral:
    def __init__(self, n, a, b, poly):
        self.n = n
        self.a = a
        self.b = b
        self.h = (b-a)/3*n
        self.xs = list(a + i*self.h for i in range((3*n)+1))
        self.ys = list(poly.designate_res_for_x(x) for x in self.xs)
        self.alphas = self.designate_aplhas()

    def designate_aplhas(self):
        n = self.n
        lst = list(ap for ap, _ in zip(cycle([3,3,2]), range((3*n)-1)))
        lst.insert(0, 1)
        lst.append(1)
        return lst

    def solution(self):
        h = self.h
        ys = self.ys
        alphas = self.alphas
        mul = lambda a,b: a*b
        return (3/8)*h*sum(list(reduce(mul, [y, ap]) for y, ap in zip(ys, alphas)))

    def average(self):
        a = self.a
        b = self.b
        return 1/(b-a)*self.solution()



