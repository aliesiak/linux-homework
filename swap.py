#!/usr/bin/env python3
x, y = map(int, input("Два числа через пробел: ").split())
a, b = x, y
print("До: ", a, b, "| id:", id(a), id(b))
a, b = b, a
print("Способ 1: ", a, b, "| id:", id(a), id(b))

