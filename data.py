import numpy as np
import pandas as pd

'''
ta klasa służy do tego aby pobrać zadane dane, podzielić je na miesiące i lata.
konstrukcja czysto programistyczna, nie związana z matematyczną częścią zadania
'''

class Data:
    def __init__(self, file):
        self.dataset = pd.read_csv(file)
        self.all_months = list(map(self.floater, [self.dataset.iloc[:, x].values for x in range(1,13)]))
        self.all_years = list(map(self.floater, [self.dataset.iloc[x, 1:].values for x in range(7)]))

    @staticmethod
    def floater(lst):
        return list(map(float, lst))

