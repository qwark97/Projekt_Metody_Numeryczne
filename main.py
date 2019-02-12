from polynomial import Polynomial
from newton_polynomial import Newton
from data import Data
from others import avg
import matplotlib.pyplot as plt

data = Data('tabelka.csv')
mcs = {1:'Sty', 2:'Lut', 3:'Mar', 4:'Kwi', 5:'Maj', 6:'Cze', 7:'Lip', 8:'Sie', 9:'Wrz', 10:'Paź', 11:'Lis', 12:'Gru'}

"""
ŚREDNIE TEMPERATURY MIESIĘCZNE
""""""
avgs = []
for mc_idx, mc in enumerate(data.all_months):
    avgs.append((mcs[mc_idx+1], avg(mc))) 
plt.scatter([mc for mc, _ in avgs], [temp for _, temp in avgs], color='Red')
plt.show()
for mc, temp in avgs:
    print(mc, temp, sep=': ')
""" 
















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
