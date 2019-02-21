import re
import matplotlib.pyplot as plt
import numpy as np


class Polynomial:
    def __init__(self, coefs): # konstruktor klasy wielomian przyjmuje jako argument liste współczynników gdzie ws[i] to element stojący przy x^i
        self.coefficients = coefs       
        self.degree = len(coefs)-1

    def designate_res_for_x(self, x): # metoda licząca wartość funkcji dla zadanego x
        coefficients, degree = self.coefficients, self.degree
        result = sum(coef*x**i for coef, i in zip(coefficients, np.arange(degree+1)))
        return result
            
    def designate_derivative(self):         # metoda, zwraca pochodną funkcji w postaci nowego obiektu klasy Polynomial
        old_coefs = self.coefficients[1:]   # w tym miejscu usuwany jest współczynnik przy x^0
        new_coefs = []
        for x, coef in enumerate(old_coefs):
            new_coefs.append(coef*(x+1))        # dla każdego stopnia potęgi wyznaczany jest nowy współczynnik zgodnie z zasadami liczenia pochodnych tego typu
        return Polynomial(new_coefs)            # rezultatem tej metody jest nowy obiekt klasy Polynomial odpowiadający obliczonej pochodnej

    def designate_derivative_nth_degree(self, n):   # metoda, która wyznacza pochodną n-tego stopnia ; również zwraca nowy obiekt klasy Polynomial
        derivative = self.coefficients
        for _ in range(n):
            derivative = self.designate_derivative()
        return derivative

    def show_function(self): # metoda wyswietla wielomian w formie zbliżonej do "ręcznej"
        coefficients_from_the_highest = self.coefficients[::-1]
        if not coefficients_from_the_highest: 
            print('0') 
            return
        powers_from_the_highest = [i for i in np.arange(len(coefficients_from_the_highest)-1, -1, -1)]
        function = ''
        for a, i in zip(coefficients_from_the_highest, powers_from_the_highest):
            a = ' + ' + str(a) if a>=0 else ' ' + str(a)
            function += a + 'x^' + str(i)
        pattern = r'(\+ 0x\^.+? )|(x\^0)|(^ *\+ )'
        function = re.sub(pattern, '', function)
        print(function)

    def plot(self, xs=None, name='Wykres funkcji', label='', show=True, color='blue'):
        if not xs: xs = [1, 13]
        plt.plot([x for x in range(0, 15)], [0 for _ in range(0, 15)], color='black') #X axis
        X_grid = np.arange(min(xs), max(xs)+0.01, 0.01)
        plt.plot(X_grid, [self.designate_res_for_x(x) for x in X_grid], color=color, label=label)
        plt.title(name)
        if label: plt.legend()
        if show: plt.show()

