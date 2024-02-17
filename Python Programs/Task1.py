#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def function(*args):
    if args:
        nums = list(map(float, args))
        result = 1.0
        for num in nums:
            result *= num
        return round(pow(result, 1 / len(nums)), 4)
    else:
        return None


if __name__ == "__main__":
    input_data = input("Введите числа через пробел: ").split()
    result = function(*input_data)
    print("Результат:", result)
    