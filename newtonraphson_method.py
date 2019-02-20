import numpy as np

'''
derivative - pochodna
Newton-Raphson - metoda stycznych
res_aproxs - przybliżenia rozwiązań

'''

class NRMethod:
    def __init__(self, poly, a, b):
        self.poly = poly                                                        # wielomian, na którym stosowana będzie metoda stycznych
        self.derivative1 = poly.designate_derivative_nth_degree(1)              # pierwsza pochodna
        self.derivative2 = poly.designate_derivative_nth_degree(2)              # druga pochodna
        self.a = a                                                              # lewa krawędź przedziału w której będzie szukane rozwiązanie
        self.b = b                                                              # prawa krawędź przedziału w której będzie szukane rozwiązanie
        self.validate()                                                         # metoda sprawdzająca czy spełnione są warunki zbieżności
        self.starting_point = self.designate_starting_point()                   # punkt startowy do wykonywania obliczeń

    def designate_starting_point(self):     # metoda, która wyznacza punkt startowy
        poly = self.poly
        derivative2 = self.derivative2
        a = self.a
        b = self.b
        if poly.designate_res_for_x(a) * derivative2.designate_res_for_x(a) > 0: return a # jeśli iloczyn wartości badanej funkcji w 'a' oraz pochodnej drugiego stopnia w 'a' jest większy od zera to punkt startowy to 'a'
        return b                                                                          # w przeciwnym wypadku punk startowy to 'b'

    def function(self, xn):  # metoda, która dla xn wyznacza xn+1
        derivative1 = self.derivative1
        poly = self.poly
        return xn - (poly.designate_res_for_x(xn) / derivative1.designate_res_for_x(xn))

    def iterate(self, n=None, eps=None): # metoda zawierająca przepis iteracyjny
        x0 = self.starting_point
        res_aproxs = [x0]   
        x_pres = x0
        if n: # jeśli podana jest planowana liczba iteracji wykonywany jest poniższy blok kodu
            for _ in range(n):
                x_next = self.function(x_pres)
                res_aproxs.append(x_next)
                x_pres = x_next
        elif eps: # jeśli podany jest epsilon wykonywany jest poniższy blok kodu
            diff = 10
            while(diff > eps):
                x_next = self.function(x_pres)
                res_aproxs.append(x_next)
                diff = abs(x_next - x_pres)
                x_pres = x_next
        else:
            raise Exception('Podaj liczbe iteracji lub epsilon')
        return res_aproxs

    def validate(self):
        a = self.a
        b = self.b
        poly = self.poly
        derivative1 = self.derivative1
        derivative2 = self.derivative2
        test_deriv = lambda lst: True if all(y<=0 for y in lst) or all(y>=0 for y in lst) else False # funkcja sprawdzająca jedyność znaku na podanej liście wartości
        scope = [a,b]                                                               # przedział, dla którego sprawdzane są wartości w kolejnych warunkach
        xs = np.arange(min(scope), max(scope), 0.1)                                 # ta konstrukcja tworzy liste 'iksów' od a do b różniących się od siebie wartością 0.1
        first = poly.designate_res_for_x(a)*poly.designate_res_for_x(b) < 0         # test pierwszego warunku zbieżności
        second = test_deriv([derivative1.designate_res_for_x(x) for x in xs])       # test drugiego warunku zbieżności
        third = test_deriv([derivative2.designate_res_for_x(x) for x in xs])        # test trzeciego warunku zbieżności
        assert all([first, second, third]), 'Warunki zbieżności nie są spełnione'   # jeśli któryś z warunków nie jest spełniony zostanie podniesiony błąd

        """ na zajęciach sprawdzaliśmy stałość znaku na pochodnych wizualnie patrząc na wykres - tutaj dzieje się to 
            analogiczne lecz 'automatycznie' - począwszy od 'a' wszystkie wartości pochodnej pierwszego, a potem drugiego stopnia
            muszą mieć taki sam znak - jeśli tak nie będzie, do zmiennej zostanie przypisana wartość False co w kolejnym etapie
            poskutkuje podniesieniem błędu """
