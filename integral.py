from itertools import cycle
from functools import reduce
import numpy as np


class Integral:
    def __init__(self, n, a, b, poly): # klasa przyjmująca jako argumenty przyjęte n, granice przedziału a i b oraz instancję klasy polynomial
        self.n = n
        self.a = a
        self.b = b
        self.h = (b-a)/(3*n )                                           # wyliczenie 'h' zgodnie ze wzorem dla liczenia całki metodą 3/8 Newtona 
        self.xs = np.arange(a, b+1, self.h)                             # w momencie tworzenia instancji wyznaczane są wartości X zgodnie ze wzorem
        self.ys = list(poly.designate_res_for_x(x) for x in self.xs)    # dla powyższych x-ów wyznaczane są wartości funkcji
        self.alphas = self.designate_aplhas()                           # w tym momencie generowana jest lista alf, zgodnie ze schematem dla 3/8 Newtona:
                                                                        # na początku i na końcu 1 a w środku 3,3,2,3,3,2,...
    def designate_aplhas(self):
        n = self.n                                                        
        lst = list(ap for ap, _ in zip(cycle([3,3,2]), range((3*n)-1)))   # w tym miejscu generowana jest cykliczna lista 3,3,2,3,3,2...
        lst.insert(0, 1)                                                  # dodanie jedynki na początku
        lst.append(1)                                                     # oraz na końcu
        return lst

    def solution(self):     # metoda, która zgodnie ze wzorem oraz wartościami podanymi w konstruktorze liczy całke oznaczoną
        h = self.h          
        ys = self.ys
        alphas = self.alphas
        mul = lambda a,b: a*b
        return (3/8)*h*sum(list(reduce(mul, [y, ap]) for y, ap in zip(ys, alphas))) # suma iloczynów par alfa i y pomnożona przez h*(3/8)

    def average(self): # metoda zwracająca średnią wartość funkcji
        a = self.a
        b = self.b
        return 1/(b-a)*self.solution() # wzrór na średnią wartość funkcji



