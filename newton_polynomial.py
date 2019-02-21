from functools import reduce
from decimal import Decimal
import re
import numpy as np
import matplotlib.pyplot as plt
from sympy import simplify
from polynomial import Polynomial

class Newton:
    def __init__(self, xs, ys): # konstruktor jako parametry przyjmuje punkty listy 'iksów' i 'igreków' na podstawie, których ma wyznaczyć interpolacje
        self.xs = xs 
        self.ys = ys
        self.Cs = self.designate_Cs()
    
    def designate_denominators(self): # metoda wyznacza dzielniki używane przy wyznaczaniu C 
        xs = self.xs
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

    def designate_counters(self, quotients): #metoda dla podanej "poprzedniej" kolumny C wyznacza liczniki do wyliczenia "następnej" kolumny C
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
        ys = self.ys
        denominators = self.designate_denominators()
        Cs = [ys[0]]
        quotients = ys
        for sub_denoms in denominators:
            counters = self.designate_counters(quotients)
            quotients = []
            for counter, denom in zip(counters, sub_denoms):
                quotients.append(counter / denom)
            Cs.append(quotients[0])
        return Cs

    def designate_res_for_x(self, x): # metoda wyznacza wartość interpolacji w podanym punkcie x 
        xs = self.xs
        Cs = self.Cs
        mul = lambda a,b: a*b
        Y = sum(Cs[i]* (reduce(mul, [x-xs[k] for k in range(i)], 1)) for i in range(len(Cs))) # suma iloczynów - wzór na interpolacje newtona
        return Y

    def designate_polynomial(self): # metoda, która na bazie wyznaczonych C oraz 'iksów' zwraca obiekt klasy wielomian, który odpowiada wielomianowi otrzymanemu z interpolacji
        Cs = list(map(Decimal, self.Cs))
        xs = self.xs[:-1]
        res = ''
        for i in range(len(Cs)): # ta pętla tworzy wersję "długą" wielomianu po interpolacji, która przy użyciu wyrażeń regularnych jest "oczyszczana" ze zbędnych elementów
            sub = '+'+str(Cs[i]) if Cs[i]>=0 else str(Cs[i])
            for j in range(i):
                sub += '*(x-%f)' % xs[j]
            res += sub
        pattern = r'(\+ 0x\^.+? )|(x\^0)|(^ *\+ )'
        res = re.sub(pattern, '', res)
        res = re.sub(r'--', '+', res)
        pol = str(simplify(res)) # importowana funkcja simplify upraszcza wersję "długą" wzoru do postaci wielomianu ze współczynnikami ułożonymi od najwyższej potęgi
        pol = pol.replace(' ', '').replace('-', ' -').replace('+',' ').strip()
        sums = pol.split(' ')
        coefs = []
        for summ in sums: # pętla z podzielonej wcześniej wersji "skróconej" wielomianu uzyskuje współczynniki
            ob = summ.strip()
            pattern = r'(\*x.*)|(x.*)'
            ob = re.sub(pattern, '', ob)
            if ob: coefs.append(float(ob))
            else: coefs.append(1.0)
        final_res = coefs[::-1]
        return Polynomial(final_res) # na bazie uzyskanych współczynników tworzony jest nowy obiekt klasy Polynomial

    def plot(self, xs=None, name='Wielomian interpolacyjny', label='', show=True, color='blue'):
        if not xs: xs = self.xs
        plt.plot([x for x in range(-2, 14)], [0 for _ in range(-2, 14)], color='black') #X axis
        X_grid = np.arange(min(xs), max(xs), 0.01)
        plt.plot(X_grid, [self.designate_res_for_x(x) for x in X_grid], color=color, label=label)
        plt.title(name)
        plt.legend()
        if show: plt.show()
                
    

