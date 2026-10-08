#!/usr/bin/env python3
n = int(input("Трехзначное число: "))
a = n // 100
b = n// 10 % 10
c = n % 10
print("Через // и %:", a + b + c, c * 100 + b * 10 + a)

