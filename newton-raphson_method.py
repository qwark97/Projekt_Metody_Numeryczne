import numpy as np
from polynomial import Polynomial

class NRMethod:
    def __init__(self, poly, a, b):
        self.poly = poly
        self.derivative1 = poly.designate_derivative_nth_degree(poly, 1)
        self.derivative2 = poly.designate_derivative_nth_degree(poly, 2)
        self.a = a
        self.b = b
        self.validate()
        self.starting_point = self.designate_starting_point()

    def designate_starting_point(self):
        poly = self.poly
        derivative2 = self.derivative2
        a = self.a
        b = self.b
        if poly.designate_res_for_x(a) * derivative2.designate_res_for_x(a) >= 0: return a
        return b

    def function(self, xn):
        derivative1 = self.derivative1
        return xn - (poly.designate_res_for_x(xn) / derivative1.designate_res_for_x(xn))

    def iterate(self, n=None, eps=None):
        x0 = self.starting_point
        res_aproxs = [x0]
        x_pres = x0
        if n:
            for _ in range(n):
                x_next = self.function(x_pres)
                res_aproxs.append(x_next)
                x_pres = x_next
        else:
            diff = 10
            while(diff > eps):
                x_next = self.function(x_pres)
                res_aproxs.append(x_next)
                diff = abs(x_next - x_pres)
                x_pres = x_next
        return res_aproxs


        
    def validate(self):
        a = self.a
        b = self.b
        poly = self.poly
        derivative1 = self.derivative1
        derivative2 = self.derivative2
        test_deriv = lambda lst: True if all(y<=0 for y in lst) or all(y>=0 for y in lst) else False
        scope = [a,b]
        xs = np.arange(min(scope), max(scope), 0.1)
        first = poly.designate_res_for_x(a)*poly.designate_res_for_x(b) < 0
        second = test_deriv([derivative1.designate_res_for_x(x) for x in xs])
        third = test_deriv([derivative2.designate_res_for_x(x) for x in xs])
        assert all([first, second, third]), 'Warunki zbieżności nie są spełnione'

poly = Polynomial([-6,1,1])

#poly.plot()
x = NRMethod(poly, -3.2, -2.8)
wyniki = x.iterate(eps=10**(-5))
print(wyniki)
