from polynomial import Polynomial
from newton_polynomial import Newton
from newtonraphson_method import NRMethod
from data import Data
from others import avg, avg_labeled
import matplotlib.pyplot as plt
import numpy as np
from math import ceil
from integral import Integral
from itertools import starmap


data = Data('tabelka.csv')
mnths = {0:'', 1:'Sty', 2:'Lut', 3:'Mar', 4:'Kwi', 5:'Maj', 6:'Cze', 7:'Lip', 8:'Sie', 9:'Wrz', 10:'Paź', 11:'Lis', 12:'Gru'}
all_years = data.all_years


"""
ŚREDNIE TEMPERATURY MIESIĘCZNE
"""
'''
avgs = list(starmap(avg_labeled, zip(list(mnths.values())[1:], data.all_months)))
plt.scatter(np.arange(1.5, 13.5), list(starmap(lambda _, temp: temp, avgs)), color='red', label='Średnie miesięczne temperatury')
plt.title('Średnie temperatury miesięczne w ciągu roku')
plt.show()

print('\nTemperatury w stopniach Celcjusza')
for mnth, temp in avgs:
    print(mnth, temp, sep=': ')
print()
'''
"""
WIELOMIAN PRZEDSTAWIAJĄCY ZMIANY TEMPERATURY W KRAKOWIE W CIĄGU ROKU
""" 
'''
# aby znaleźć wielomian najbardziej pasujący do posiadanych wartości
# sprawdzam jak na wykresie pokrywają się wartości posiadane
# dla konkretnych miesięcy z wartościami
# wyliczonymi przy użyciu interpolacji Newtona


for i in range(7): # pętla po latach
    plt.plot(np.arange(-1, 16), [0 for _ in np.arange(-1, 16)], color='black', label='Oś X')
    
    interpolation = Newton(np.arange(1.5, 13.5), all_years[i]) # stworzenie instancji klasy tworzącej interpolacje
    
    interpolation.plot(name="Temperatury w ciągu roku"+' 201'+str(i), label='Wykres wielomianu', show=False)
    plt.scatter(np.arange(1.5, 13.5), all_years[i], color='red', label='Średnie miesięczne temperatury w danym roku') 
    plt.scatter([mnths[t] for t in np.arange(0, 13)], np.arange(0, 13), color='white') 


    plt.title("Temperatury w ciągu roku"+' 201'+str(i))                
    plt.show()                                                 


# jako, że niemalże wszystkie powyższe wykresy na bazie posiadanych danych,
# początku oraz na końcu mają znaczne odchylenia od oczekiwanych wartości,
# sprawdzam interpolację wielomianu utworzonego na bazie średnich temperatur miesięcznych  



avgs = list(map(avg, data.all_months))     # licze średnią temp. w danych miesiacach

# aby ominąć efekt Rungego, z którego to powodu w poprzednich wykresach występowały takie wahania,
# dodaję na początku i na końcu zestawu danych po dwa dodatkowe miesiące;
# interpolacja odbywa się na średnich temperaturach miesięcznych
# zaczynając od listopadowej, przechodząc przez pełny rok i kończąc na lutowej włącznie

avgs.insert(0, avgs[-1])
avgs.insert(0, avgs[-2])  # dodanie wspomnianych dodatkowych punktów
avgs.append(avgs[2])     
avgs.append(avgs[3])     

plt.plot(np.arange(-1, 16), [0 for _ in np.arange(-1, 16)], color='black', label='Oś X')

interpolation = Newton(np.arange(-0.5, 15.5), avgs)
interpolation.plot(name='Interpolacja wielomianu przy przyjętych punktach', label='Pełna interpolacja', show=False)

plt.plot(np.arange(1, 13+0.001, 0.001), [interpolation.designate_res_for_x(x) for x in np.arange(1, 13+0.001, 0.001)],
         color='green', label='Wielomian przedstawiający zmiany temperatur w ciągu roku')
plt.scatter(np.arange(1.5, 13.5), avgs[2:-2], color='red', label='Średnie miesięczne temperatury')

plt.scatter([mnths[t] for t in np.arange(0, 13)], np.arange(0, 13), color='white') # ta linia jedynie ułatwia mi odpowiednie oznaczenie wykresu
plt.legend()
plt.show()
'''
"""
SZUKANIE DNI DLA TEMPERATUR UJEMNYCH ORAZ DODATNICH UŻYWAJĄC METOD PRZYBLIŻONYCH - TUTAJ METODY SIECZNYCH
""" 
'''
# ponowne wynaczenie wielomianu wybranego na poprzednim etapie
avgs = list(map(avg, data.all_months))   
avgs.insert(0, avgs[-1])
avgs.insert(0, avgs[-2]) 
avgs.append(avgs[2])     
avgs.append(avgs[3]) 

# utworzenie obiektu klasy wielomian z interpolacji Newtona
interpolation = Newton(np.arange(-0.5, 15.5), avgs)
polynomial = interpolation.designate_polynomial() 
polynomial.plot([1, 13], name='Wielomian przedstawiający zmiany temperatur w ciągu roku', color='green') 

# na bazie wykresu wyznaczam przedziały, w których szukane będą pierwiastki wielomianu
scopes = [(2, 2.5), (12.5, 13)]
results = []

for scope in scopes:
    a, b = scope
    method = NRMethod(polynomial, a, b)
    approx = method.iterate(eps=10**(-5))
    results.append(approx)

for point, approxs in zip(scopes, results):
    print('Kolejne przybliżenia pierwiastka w przedziale', point, ':', '\n', approxs)

# szacuje konkretne dni w których temperatura zmienia się 
# z ujemnej na dodatnią i na odwrót aby ocenić 
# kiedy temperatura jest ujemna oraz dodatnia
first_change = str(ceil((results[0][-1] - int(results[0][-1]) ) * 30))+'.%02d' % int(results[0][-1])
secon_change = str(ceil((results[1][-1] - int(results[1][-1]) ) * 30))+'.%02d' % int(results[1][-1])

print(
    """\n\tW dniach od 01.01 do {} średnia temperatura była ujemna.
       Następnie średnia temperatura aż do dnia {} była dodatnia. 
       Po wspomnianej dacie, średnia temperatura już 
       do końca roku była ujemna.\n""".format(first_change, secon_change)
)



'''
"""
SZUKANIE NAJCIEPLEJSZEGO I NAJZIMNIEJSZEGO DNIA W ROKU
"""
'''
avgs = list(map(avg, data.all_months))   
avgs.insert(0, avgs[-1])
avgs.insert(0, avgs[-2]) 
avgs.append(avgs[2])     
avgs.append(avgs[3]) 

interpolation = Newton(np.arange(-0.5, 15.5), avgs)
polynomial = interpolation.designate_polynomial()
polynomial.plot([1, 13])
derivative = polynomial.designate_derivative()
derivative.plot([1, 13], name='Wykres pochodnej funkcji')

#szukam y=0 dla pochodnej w przedziale wybranym na bazie wykresu
scope = [7.7, 7.8]
method = NRMethod(derivative, scope[0], scope[1])
approx = method.iterate(eps=10**(-5))
x = approx[-1]
min_or_max = ('Znalezione x to maximum lokalne funkcji' if derivative.designate_res_for_x(x-0.001) > 0 
                                                        else 'Znaleziony x to minimum lokalne funkcji')
print(min_or_max)
hottest = str(ceil((x - int(x)) * 30))+'.%02d' % int(x)
print('Najciepleszy dzień w roku przypadał na %s' % hottest)

# jako, że otrzymany wielomian nie ma jako tako minimum lokalnego 
# szukam najzimniejszego dnia na początku oraz na końcu wykresu

coldest = min((1, polynomial.designate_res_for_x(1)), (13, polynomial.designate_res_for_x(13)), key=lambda x: x[1])[0]
print('Najzimniejszy dzien w roku przypadał na {}'.format('01.01' if coldest is 1 else '31.12'))
'''
"""
WYLICZENIE ZA POMOCĄ ŚREDNIEJ CAŁKOWEJ ŚREDNIEJ TEMPERATURY W ROKU
"""

avgs = list(map(avg, data.all_months))   
avgs.insert(0, avgs[-1])
avgs.insert(0, avgs[-2]) 
avgs.append(avgs[2])     
avgs.append(avgs[3]) 

interpolation = Newton(np.arange(-0.5, 15.5), avgs)
polynomial = interpolation.designate_polynomial()

for n in range(1, 21):
    integral = Integral(n, 1, 13, polynomial)
    print('Wartość dla n =', n,': ', integral.solution())

# Wartość całki normuje się dla n = 6 dlatego dla takiego n policzę średnią

integral = Integral(6, 1, 13, polynomial)
average_temp = integral.average()

print('Średnia dobowa temperatura w roku w Polsce wynosiła ok.', round(average_temp, 2), 'stopni Celsjusza')

