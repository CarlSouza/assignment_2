import numpy as np
import pandas as pd
import sourcedefender
from exercises import exercise4
from solutions import exercise4 as solution4


def test4():
    with open('songs.txt') as file:
        sers = file.read().split('\n\n\n')
        sers = [
            ser.replace('\n\n', '. ').replace('\n',
                                              ', ').replace('.',
                                                            ' . ').replace(',',
                                                                           ' , ').lower()
            for ser in sers
        ]
        sers = [pd.Series(ser.split()) for ser in sers]

    for ser1 in sers:
        size = len(ser1)
        for t in range(1, 11):
            start, end = np.random.randint(0, size), np.random.randint(0, size)
            start, end = min(start, end), max(start, end)
            ser2 = ser1[start:end].copy().reset_index(drop=True)
            for index in range(1, len(ser2), 2):
                if np.random.random() < 1 / 3:
                    ser2[index] = np.nan

            assert (solution4(ser1.copy(),
                              ser2.copy()) == exercise4(ser1.copy(), ser2.copy())).all()
