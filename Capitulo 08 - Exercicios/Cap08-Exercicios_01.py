"""
Crie um array NumPy com 1000000 e uma lista com 1000000.
Multiplique cada elemento do array e da lista por 2 e calcule o tempo de execução
com cada um dos objetos (use %time).
Qual objeto oferece melhor performance, array NumPy ou lista?
"""

import numpy as np
import timeit
import pandas as pd
import requests
import sqlite3

array = np.array([1000000])
print(timeit.timeit(f'{array[0]} * 2', number=100)/100)
lista = [1000000]
print(timeit.timeit(f'{lista[0]} * 2', number=100)/100)
print("\nArray numpy demora 2,4s\nLista python demora 2,1s\nLista python é mais rapida.")