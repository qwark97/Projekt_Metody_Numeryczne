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

# ponowne wynaczenie wielomianu wybranego na poprzednim etapie

avgs = list(map(avg, data.all_months))       
avgs.insert(0, avgs[-1])
avgs.insert(0, avgs[-2]) 
avgs.append(avgs[2])     
avgs.append(avgs[3]) 

interpolation = Newton(np.arange(-0.5, 15.5), avgs)
interpolation.plot([-0.5, 15.5], show=False, label='interpolacja', color='green')

#print('C wyliczone przeze mnie:', interpolation.Cs)

polynomial = interpolation.designate_polynomial()    # utworzenie obiektu klasy wielomian z interpolacji Newtona
polynomial.plot([-0.5, 15.5], name='Wielomian przedstawiający zmiany temperatur w ciągu roku', show=False, label='wielomian', color='red') # na bazie wykresu wyznaczam przedziały, w których szukane będą pierwiastki wielomianu



#plt.legend()
#plt.show()

#fst = interpolation.designate_res_for_x(0)
#scd = polynomial.designate_res_for_x(0)
#print(fst, scd, sep='\n')


#met_stycznych = NRMethod(wielomian, 0.04, 0.05)

#wyniki = met_stycznych.iterate(eps=10**(-5))

#print(wyniki)

#dzien = print(ceil(wyniki[-1]/365))


"""
WYLICZENIE ZA POMOCĄ ŚREDNIEJ CAŁKOWEJ ŚREDNIEJ TEMPERATURY W ROKU
"""
'''

# ponowne wynaczenie wielomianu wybranego na poprzednim etapie

avgs = []                                           
for mnth_idx, mnth in enumerate(data.all_months):   
    avgs.append((mnths[mnth_idx], avg(mnth)))       

closests_temps = []
for avg, temps in zip(avgs, data.all_months):
    closest = temps[0]                      
    new_dis = abs(temps[0] - avg[1])                
    old_dis = new_dis                               
    for temp in temps:                              
        new_dis = abs(temp-avg[1])                  
        if new_dis < old_dis:                       
            old_dis = new_dis
            closest = temp
    closests_temps.append((avg[0], closest))

interpolacja2 = Newton([x for x in range(12)], [temp for _, temp in closests_temps])
wielomian = interpolacja2.designate_polynomial()
#wielomian.plot([0, 11])

calka = Integral(3, 3, 11, wielomian)

sr_temp = calka.average()

print(sr_temp)

'''