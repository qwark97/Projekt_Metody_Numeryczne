from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
from sympy import simplify
import re
from polynomial import Polynomial
from decimal import Decimal

'''
counter - licznik
denominator - dzielnik
minuend - odjemna
subtrahend - odjemnik
quotients - wyniki dzielenia przy wyznaczaniu C
'''

class Newton:
    def __init__(self, xs, ys): # konstruktor jako parametry przyjmuje punkty (x,y) na podstawie, których ma wyznaczyć interpolacje
        self.xs = xs 
        self.ys = ys
        self.Cs = self.designate_Cs()
    
    @staticmethod
    def designate_denominators(xs): #metoda wyznacza dzielniki używane przy wyznaczaniu C 
        denoms = []
        sub_minuend = 1
        sub_subtrahend = 1
        idx = len(xs) - 1
        for _ in range(idx, 0, -1):
            sub_denoms = []
            for j in range(sub_minuend, idx+1):
                minuend = xs[j]
                subtrahend = xs[j-sub_subtrahend]
                sub_denoms.append( minuend - subtrahend )
            denoms.append(sub_denoms)
            sub_minuend += 1
            sub_subtrahend += 1
        return denoms

    @staticmethod
    def designate_counters(quotients): #metoda dla podanej "poprzedniej" kolumny C wyznacza liczniki do wyliczenia "następnej" kolumny C
        counters = []
        sub_minuend = 1
        sub_subtrahend = 1
        idx = len(quotients) - 1
        for _ in range(idx, 0, -1):
            for j in range(sub_minuend, idx+1):
                minuend = quotients[j]
                subtrahend = quotients[j-sub_subtrahend]
                counters.append( minuend - subtrahend )
        return counters
    
    def designate_Cs(self): #metoda wyznacza parametry C dla punktów podanych do konstruktora
        xs = self.xs 
        ys = self.ys
        denominators = self.designate_denominators(xs)
        Cs = [ys[0]]
        quotients = ys
        for sub_denoms in denominators:
            counters = self.designate_counters(quotients)
            quotients = []
            for counter, denom in zip(counters, sub_denoms):
                quotients.append(counter / denom)
            Cs.append(quotients[0])
        return Cs

    def designate_res_for_x(self, x):
        xs = self.xs
        Cs = self.Cs
        mul = lambda a,b: a*b
        Y = sum(Cs[i]* (reduce(mul, [x-xs[k] for k in range(i)], 1)) for i in range(len(Cs)))
        return Y

    def designate_polynomial(self):
        Cs = list(map(Decimal, self.Cs))
        xs = self.xs[:-1]
        res = ''
        for i in range(len(Cs)):
            sub = '+'+str(Cs[i]) if Cs[i]>=0 else str(Cs[i])
            for j in range(i):
                sub += '*(x-%d)' % xs[j]
            res += sub
        pattern1 = r'\+ 0x\^.+? '
        pattern2 = r'x\^0'
        pattern3 = r'^ *\+ '
        for pattern in [pattern1, pattern2, pattern3]:
            res = re.sub(pattern, '', res)
        res = re.sub(r'--', '+', res)
        pol = str(simplify(res))
        pol = pol.replace(' ', '').replace('-', ' -').replace('+',' ').strip()
        sums = pol.split(' ')
        coefs = []
        for summ in sums:
            ob = summ.strip()
            ob = re.sub(r'\*x.*', '', ob)
            coefs.append(float(ob))
        final_res = coefs[::-1]
        return Polynomial(final_res)



    def plot(self, xs=None, name='Wielomian interpolacyjny', shift_X=0, shift_Y=0, xlabel=''):
        if not xs: xs = self.xs
        #plt.plot([0+shift_X for _ in range(-1, 13)], range(-1, 13), color='black') #Y axis
        plt.plot([x+shift_X for x in range(-1, 13)], [0+shift_X for _ in range(-1, 13)], color='black') #X axis
        X_grid = np.arange(min(xs), max(xs), 0.01)
        plt.plot(X_grid, [self.designate_res_for_x(x) for x in X_grid], color='blue')
        plt.title(name)
        plt.xlabel(xlabel)
        plt.show()
                
    

