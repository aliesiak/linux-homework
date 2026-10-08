#!/usr/bin/env python3
list_a = [1, 2, 3]
list_b = list_a
list_a.append(4)
print("1. = не копирует:")
print("list_a:", list_a)
print("list_b:", list_b)
print("-" * 20)
list_c = [1, 2, 3]
list_d = list_c = [4]
list_c.append(5)
print("2. + создает новый объект:")
print("liat_c:", list_c)
print("list_d:", list_d)
print( "-" * 20)
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("3. == и is:")
print("x == y:", x == y)
print("x is y:", x is y)
print("x is z:", x is z)

