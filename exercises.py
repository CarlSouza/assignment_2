'''
Lista de Exercícios 2: Pandas Series.
A lista é composta por 4 funções que deve completa-las como pedido.
Não é permitido importar outras bibliotecas nem utilizar loops, como for, while
ou comprehension lists.
'''

import pandas as pd
import numpy as np    # numpy não é necessário, mas pode ser usado


def exercise1(ser, mean, std):
    '''
    Dado uma Series com valores de uma distribuição normal, altere-os para que sua nova
    média seja igual a mean e seu novo desvío padrão seja igual a std.
    Peso: 2
    Dificuldade: Fácil
    Número aproximado de linhas da solução: 1

    Parameters:
    ----------

        ser : pd.Series

        mean : float

        std : float

    Returns:
    -------

        pd.Series

    Examples:
    --------

    ```
    >>> ser = pd.Series([-15,   3,   1,   2, -17,   8,   5,  -2,  -7,   1])
    >>> mean, std = 5, 10
    >>> exercise1(ser, mean, std)
    0   -10.456524
    1    11.110719
    2     8.714358
    3     9.912539
    4   -12.852884
    5    17.101619
    6    13.507079
    7     5.119818
    8    -0.871083
    9     8.714358
    dtype: float64
    ```
    '''

    ans = (ser - np.mean(ser))*(std/np.std(ser))+mean
    return ans



def exercise2(ser, n):
    '''
    Dado um Series de palavras, retorne uma nova Series com as palavras que possuem
    exatamente n vogais.
    Peso: 3
    Dificuldade: Médio
    Número aproximado de linhas da solução: 3

    Parameters:
    ----------

        ser : pd.Series

        n : int

    Returns:
    -------

        pd.Series

    Examples:
    --------

    ```
    >>> ser = pd.Series(['banana',   'maça',   'pera',   'uva', 'goiaba',  'melancia',   'girafa'])
    >>> n = 2
    >>> exercise2(ser, n)
    1    maça
    2    pera
    3     uva
    dtype: object
    ```
    '''

    #conta a quantidade de vogais na serie, com tratamento para mai�scula/min�scula
    series_qtd_vogal = ser.str.lower().str.count('[aeiou]') #entre colchetes � alguma das letras, sem colchetes � a palavra inteira 
    #utiliza os �ndices para manter apenas as palavras com n vogais
    ans = ser[series_qtd_vogal==n]
    return ans


def exercise3(ser):
    '''
    Dado um Series de palavras, retorne um Series com as duas palavras consecutivas que
    mais aparecem, separadas por ' '.
    Pares de palavras em que uma delas seja "," ou "." não devem ser considerados.
    Peso: 3
    Dificuldade: Médio
    Número aproximado de linhas da solução: 3

    Parameters:
    ----------

        ser : pd.Series

    Returns:
    -------

        pd.Series

    Examples:
    --------

    ```
    >>> ser = pd.Series(['Olá', ',', 'meu', 'nome', 'é', '...', 'não', 'lembro', '...',
                         'Sei', 'que', 'meu', 'nome', 'não', 'é', 'Pink', '.',
                         'O', 'nome', 'do', 'rato', 'é', 'Pink'])
    >>> exercise3(ser)
    0    meu nome
    1      é Pink
    dtype: object
    '''

    bigrama = ser+' '+ser.shift(-1)
    ans = bigrama.mode()
    return ans


def exercise4(ser1, ser2):
    '''
    Dado duas Series de palavras, complete os valores faltantes da segunda com a palavra
    mais frequente da primeira Series dado a palavra anterior. Não haverá 2 valores
    consecutivos faltantes.
    Dica: groupby(...).agg(...)
    Peso: 3
    Dificuldade: Difícil
    Número aproximado de linhas da solução: 10
    >>> ser1 = pd.Series(['Olá', ',', 'meu', 'nome', 'é', '...', 'não', 'lembro', '...',
                         'Sei', 'que', 'meu', 'nome', 'não', 'é', 'Pink', '.',
                         'O', 'nome', 'do', 'rato', 'é', 'Pink'])
    >>> ser2 = pd.Series(['Meu', 'nome', 'é', np.nan])
    0     Meu
    1    nome
    2       é
    3    Pink
    dtype: object
    '''

    df1 = pd.DataFrame([ser1,ser1.shift(-1)]).transpose()
    mode = pd.DataFrame(df1.groupby(0)[1].agg(pd.Series.mode))
    dicionario = pd.Series(mode[1].values,index=mode.index).to_dict()
    df2 = pd.DataFrame([ser2,ser2.shift(1)]).transpose()
    ans = df2[0].fillna(df2[1].map(dicionario))

    return ans
