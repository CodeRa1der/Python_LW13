#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def function(*args):
    if args:
        nums = list(map(float, args))
        function_sum = sum(1 / num for num in nums)
        return round(len(nums) / function_sum, 4)
    else:
        return None


if __name__ == "__main__":
    input_data = input("Введите числа через пробел: ").split()
    result = function(*input_data)
    print("Результат:", result)
