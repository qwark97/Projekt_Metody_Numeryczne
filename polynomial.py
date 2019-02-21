import re
import matplotlib.pyplot as plt
import numpy as np

'''
coefficients - współczynniki
degree - stopień wielomianu
function - funkcja w znaczeniu wielomian
power - w znaczeniu wykładnik
'''

class Polynomial:
    def __init__(self, coefs): #konstruktor klasy wielomian przyjmuje jako argument liste współczynników gdzie ws[i] to element stojący przy x^i
        self.coefficients = coefs       
        self.degree = len(coefs)-1

    def designate_res_for_x(self, x): #metoda licząca wartość funkcji dla zadanego x
        coefficients, degree = self.coefficients, self.degree
        result = sum(coef*x**i for coef, i in zip(coefficients, range(degree+1)))
        return result
            
    def designate_derivative(self):         # metoda, która dla przekazanej funkcji zwraca jej pochodną w postaci instancji klasy Polynomial
        old_coefs = self.coefficients[1:]   # w tym miejscu usuwany jest współczynnik przy x^0
        new_coefs = []
        for x, coef in enumerate(old_coefs):
            new_coefs.append(coef*(x+1))        # dla każdego stopnia potęgi wyznaczany jest nowy współczynnik zgodnie z zasadami liczenia pochodnych tego typu
        return Polynomial(new_coefs)            # rezultatem tej metody jest nowa instancja klasy Wielomian odpowiadająca pochodnej funkcji przekazanej jako argument

    def designate_derivative_nth_degree(self, n):   # metoda, która dla przekazanej funkcji zwraca jej pochodną n-tego stopnia
        derivative = self.coefficients
        for _ in range(n):
            derivative = self.designate_derivative()
        return derivative

    def show_function(self): # metoda wyswietla wielomian w formie zbliżonej do "ręcznej"
        coefficients_from_the_highest = self.coefficients[::-1]
        if not coefficients_from_the_highest: 
            print('0') 
            return
        powers_from_the_highest = [i for i in range(len(coefficients_from_the_highest)-1, -1, -1)]
        function = ''
        for a, i in zip(coefficients_from_the_highest, powers_from_the_highest):
            a = ' + ' + str(a) if a>=0 else ' ' + str(a)
            function += a + 'x^' + str(i)
        pattern1 = r'\+ 0x\^.+? '
        pattern2 = r'x\^0'
        pattern3 = r'^ *\+ '
        for pattern in [pattern1, pattern2, pattern3]:
            function = re.sub(pattern, '', function)
        print(function)

    def plot(self, xs=None, name='Wykres funkcji', label='', show=True, color='blue'):
        if not xs: xs = [-5, 5]
        plt.plot([x for x in range(0, 15)], [0 for _ in range(0, 15)], color='black') #X axis
        X_grid = np.arange(min(xs), max(xs)+0.01, 0.01)
        plt.plot(X_grid, [self.designate_res_for_x(x) for x in X_grid], color=color, label=label)
        plt.title(name)
        if label: plt.legend()
        if show: plt.show()

