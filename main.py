from polynomial import Polynomial
from newton_polynomial import Newton
from newtonraphson_method import NRMethod
from data import Data
from others import avg
import matplotlib.pyplot as plt
import numpy as np
from math import ceil
from integral import Integral

# NOTKA DLA MNIE
# są jakieś błędy z wykresami, źle pokazuje scatter - sprawdzić czy ta interpolacja na pewno jest dobra


data = Data('tabelka.csv')
mnths = {0:'Sty', 1:'Lut', 2:'Mar', 3:'Kwi', 4:'Maj', 5:'Cze', 6:'Lip', 7:'Sie', 8:'Wrz', 9:'Paź', 10:'Lis', 11:'Gru'}

"""
ŚREDNIE TEMPERATURY MIESIĘCZNE
""""""
avgs = []
for mnth_idx, mnth in enumerate(data.all_months):
    avgs.append((mnths[mnth_idx+1], avg(mnth))) 
plt.scatter([mnth for mnth, _ in avgs], [temp for _, temp in avgs], color='Red')
plt.show()
for mnth, temp in avgs:
    print(mnth, temp, sep=': ')
""" 



"""
WIELOMIAN PRZEDSTAWIAJĄCY ZMIANY TEMPERATURY W KRAKOWIE W CIĄGU ROKU
""" """
all_mnths = data.all_months
all_years = data.all_years





# aby znaleźć wielomian najbardziej pasujący do posiadanych wartości
# sprawdzam jak na wykresie pokrywają się wartości posiadane
# dla konkretnych miesięcy z wartościami
# wyliczonymi przy użyciu interpolacji Newtona
 
   

for i in range(7):
    rok = all_years[i]
    interpolacja1 = Newton([x for x in range(12)], [temp for temp in all_years[i]])    # stworzenie obiektu zawierającego interpolacje

    plt.plot([x for x in range(-1, 13)], [0 for _ in range(-1, 13)], color='black')     # czarna linia na wykresie y=0       

    plt.scatter(mnths.values(), [interpolacja1.designate_res_for_x(x) for x in mnths.keys()], color='red') # czerwone punkty na wykresie odpowiadające średnim temperaturom w danych miesiącach
    X_grid = np.arange(0, 11, 0.01)                                               
    plt.plot(X_grid, [interpolacja1.designate_res_for_x(x) for x in X_grid], color='green') # zielona linia przedstawiająca wykres funkcji uzyskanej z interpolacji    

    plt.title("Temperatury w ciągu roku"+' 201'+str(i))                
    plt.xlabel("Miesiące")                                         
    plt.show()                                                 


# jako, że niemalże wszystkie powyższe wykresy na początku oraz na końcu mają znaczne odchylenia od oczekiwanych wartości, sprawdzam wielomian
# utworzony na bazie temperatur miesięcznych najbliższych średniej temperaturze w ciągu badanych 
# siedmiu lat w danycm miesiącu


avgs = []                                           #
for mnth_idx, mnth in enumerate(data.all_months):   # licze srednie temp. w danych miesiacach
    avgs.append((mnths[mnth_idx], avg(mnth)))       #

closests_temps = []
for avg, temps in zip(avgs, data.all_months):
    closest = temps[0]                      
    new_dis = abs(temps[0] - avg[1])                #
    old_dis = new_dis                               # wybieram temperaturę z danego miesiąca
    for temp in temps:                              # która jest najbardziej zbliżona sredniej temperaturze
        new_dis = abs(temp-avg[1])                  # w danym miesiącu w badanym okresie czasu
        if new_dis < old_dis:                       #
            old_dis = new_dis
            closest = temp
    closests_temps.append((avg[0], closest))


# wykres przedstawiający wartości wybrane 
# w poprzednim paragrafie oraz wykres  
# wielomianu interpolacyjnego Newtona 
# wyliczony na podstawie tych wartości

interpolacja2 = Newton([x for x in range(12)], [temp for _, temp in closests_temps])

plt.plot([x for x in range(-1, 13)], [0 for _ in range(-1, 13)], color='black')

plt.scatter(mnths.values(), [interpolacja2.designate_res_for_x(x) for x in mnths.keys()], color='red') 
X_grid = np.arange(0, 11, 0.01)                                               
plt.plot(X_grid, [interpolacja2.designate_res_for_x(x) for x in X_grid], color='green')             
                                                                                                    
plt.title("Wykres funkcji na bazie srednich miesięcznych temperatur w latach 2010-2016")            
plt.xlabel("Miesiące")                                                                              
plt.show()


#otrzymany wielomian interpolacyjny najbardziej pasuje do punktów, z których został utworzony 
#dlatego to właśnie jego będę używał do dalszych obliczeń

""" 

"""
SZUKANIE DNI DLA TEMPERATUR UJEMNYCH ORAZ DODATNICH UŻYWAJĄC METOD PRZYBLIŻONYCH - TUTAJ METODY SIECZNYCH
""" """
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


wielomian = interpolacja2.designate_polynomial()                # utworzenie obiektu klasy wielomian z interpolacji Newtona
wielomian.plot([0,11], name='Wykres temperatur w ciągu roku')   # na bazie wykresu wyznaczam przedziały, w których szukane będą pierwiastki wielomianu


met_stycznych = NRMethod(wielomian, 0.04, 0.05)

wyniki = met_stycznych.iterate(eps=10**(-5))

print(wyniki)

dzien = print(ceil(wyniki[-1]/365))

"""



"""
WYLICZENIE ZA POMOCĄ ŚREDNIEJ CAŁKOWEJ ŚREDNIEJ TEMPERATURY W ROKU
"""

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