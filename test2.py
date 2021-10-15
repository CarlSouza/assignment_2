import numpy as np
import pandas as pd
import sourcedefender
from exercises import exercise2
from solutions import exercise2 as solution2


def test2():
    alphabet = tuple('qwertyuiopasdfghjklzxcvbnm')
    for t in range(1, 11):
        size = t * 1000
        n = np.random.randint(0, t)
        ser = pd.Series(
            [''.join(np.random.choice(alphabet, size=5 * n)) for _ in range(size)])

        assert (solution2(ser.copy(), n) == exercise2(ser.copy(), n)).all()
