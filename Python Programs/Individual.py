#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def function(*args):
    negative_num = False
    result = 0
    if args:
        for num in args:
            num = int(num)
            if negative_num == True:
                result += abs(num)
            elif num < 0 and negative_num == False:
                negative_num = True
        if negative_num == False:
            return 0
        return result
    else:
        return None

if __name__ == "__main__":
    input_args = input("Введите значения (для корректного выполнения добавьте отрицательное число): ").split()

    print("Результат:", function(*input_args))
