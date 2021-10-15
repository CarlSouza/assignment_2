import numpy as np
import pandas as pd
import sourcedefender
from exercises import exercise3
from solutions import exercise3 as solution3


def test3():
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

    for ser in sers:
        assert (solution3(ser.copy()) == exercise3(ser.copy())).all()
