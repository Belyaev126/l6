# !/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 16
# В списке, состоящем из вещественных элементов, вычислить:
# 1) количество положительных элементов списка;
# 2) произведение элементов списка, расположенных после последнего элемента, равного нулю.
# Преобразовать список таким образом, чтобы сначала располагались все элементы, целая часть
# которых не превышает 1, а потом - все остальные.



if __name__ == '__main__':
    a = list(map(float, input("Ввод чисел:").split()))
    r = 0

    for i in a:
        if i > 0:
            r += i
    print("1)""%.2f" % r)

    S = []
    a_min = a_max = a[0]
    i_min = i_max = 0
    b = [abs(i) for i in a]
    for i, item in enumerate(b):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item
    a_new = a[i_min:i_max+1]
    res = 1
    for j in a_new:
        res *= j
    print(res)
    a.sort()
    print(f"2) {a} ")
