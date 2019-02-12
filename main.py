from polynomial import Polynomial
from newton_polynomial import Newton
from data import Data
from others import avg
import matplotlib.pyplot as plt
import numpy as np

# NOTKA DLA MNIE
# są jakieś błędy z wykresami, źle pokazuje scatter - sprawdzić czy ta interpolacja na pewno jest dobra


data = Data('tabelka.csv')
mnths = {1:'Sty', 2:'Lut', 3:'Mar', 4:'Kwi', 5:'Maj', 6:'Cze', 7:'Lip', 8:'Sie', 9:'Wrz', 10:'Paź', 11:'Lis', 12:'Gru'}

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
"""
all_mnths = data.all_months
all_years = data.all_years

#plt.plot([0-10 for _ in range(-1000, 1000, 1)], range(-1000, 1000, 1), color='black') #Y axis
#plt.plot([x for x in range(-1000+1, 1000+1, 1)], [0 for _ in range(-1000+0, 1000+0, 1)], color='black') #X axis


for i in range(7):
    plt.plot([x for x in range(0, 13, 1)], [0 for _ in range(0, 13, 1)], color='black')
    poly = Newton([x for x in range(12)], [temp for temp in all_years[i]])                               #
    X_grid = np.arange(min(poly.xs), max(poly.xs), 0.01)                                                 # aby znaleźć wielomian najbardziej pasujący do posiadanych wartości
    plt.plot(X_grid, [poly.designate_res_for_x(x) for x in X_grid], color='green')                       # sprawdzam jak na wykresie pokrywają się wartości posiadane
    plt.scatter(mnths.values(), [poly.designate_res_for_x(x-1) for x in mnths.keys()], color='red')      # dla konkretnych miesięcy z wartościami
    plt.title("Temperatury w ciągu roku"+' 201'+str(i))                                                  # wyliczonymi przy użyciu interpolacji Newtona
    plt.xlabel("Miesiące")                                                                               #   
    plt.show()                                                                                          


# jako, że wszystkie powyższe wykresy na początku oraz na końcu mają znaczne odchylenia od oczekiwanych wartości, sprawdzam wielomian
# utworzony na bazie temperatur miesięcznych najbliższych średniej temperaturze w ciągu badanych 
# siedmiu lat w danycm miesiącu


avgs = []                                           #
for mnth_idx, mnth in enumerate(data.all_months):   # licze srednie temp. w danych miesiacach
    avgs.append((mnths[mnth_idx+1], avg(mnth)))     #

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


poly1 = Newton([x for x in range(12)], [temp for _, temp in closests_temps])
X_grid = np.arange(min(poly1.xs), max(poly1.xs), 0.01)                                              #
plt.plot(X_grid, [poly1.designate_res_for_x(x) for x in X_grid], color='blue')                      # wykres przedstawiający wartości wybrane 
plt.scatter(mnths.values(), [poly1.designate_res_for_x(x-1) for x in mnths.keys()], color='red')    # w poprzednim paragrafie oraz wykres 
                                                                                                    # wielomianu interpolacyjnego Newtona 
plt.title("Wykres funkcji na bazie srednich miesięcznych temperatur w latach 2010-2016")            # wyliczony na podstawie tych wartości
plt.xlabel("Miesiące")                                                                              #
plt.show()


#otrzymany wielomian interpolacyjny najbardziej pasuje do oczekiwanych wartości dlatego to właśnie jego będę używał do dalszych obliczeń

""""""














'''
styczen = data.all_months[0]
x = Newton([x for x in range(2010, 2017)], styczen)
x.plot([x for x in range(2010, 2017)], "Temperatury w styczniu w latach 2010-2016", shift_X=2010)

luty = data.all_months[1]
x = Newton([x for x in range(2010, 2017)], luty)
x.plot([x for x in range(2010, 2017)], "Temperatury w lutym w latach 2010-2016", shift_X=2010)

marzec = data.all_months[2]
x = Newton([x for x in range(2010, 2017)], marzec)
x.plot([x for x in range(2010, 2017)], "Temperatury w marcu w latach 2010-2016", shift_X=2010)

kwiecien = data.all_months[3]
x = Newton([x for x in range(2010, 2017)], kwiecien)
x.plot([x for x in range(2010, 2017)], "Temperatury w kwietniu w latach 2010-2016", shift_X=2010)

maj = data.all_months[4]
x = Newton([x for x in range(2010, 2017)], maj)
x.plot([x for x in range(2010, 2017)], "Temperatury w maju w latach 2010-2016", shift_X=2010)

czerwiec = data.all_months[5]
x = Newton([x for x in range(2010, 2017)], czerwiec)
x.plot([x for x in range(2010, 2017)], "Temperatury w czerwcu w latach 2010-2016", shift_X=2010)

lipiec = data.all_months[6]
x = Newton([x for x in range(2010, 2017)], lipiec)
x.plot([x for x in range(2010, 2017)], "Temperatury w lipcu w latach 2010-2016", shift_X=2010)
'''
