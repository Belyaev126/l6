#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 3.
# Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.

import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))
    if len(a) != 10:
        print('Список должен состоять из 10 элементов', file=sys.stderr)

    i_min = a.index(min(a))
    a[0], a[i_min] = a[i_min], a[0]
    print(a)
