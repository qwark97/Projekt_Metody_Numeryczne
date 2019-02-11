from polynomial import Polynomial
from newton_polynomial import Newton
from data import Data

data = Data('tabelka.csv')

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

