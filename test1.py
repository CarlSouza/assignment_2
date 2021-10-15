import numpy as np
import pandas as pd
import sourcedefender
from exercises import exercise1
from solutions import exercise1 as solution1


def test1():
    for t in range(1, 11):
        size = t * 1000
        ser = pd.Series(
            np.random.normal(loc=t * np.random.random(),
                             scale=t * np.random.random(),
                             size=size))
        mean = t * np.random.random()
        std = t * np.random.random()

        assert (solution1(ser.copy(), mean, std) == exercise1(ser.copy(), mean,
                                                              std)).all()
