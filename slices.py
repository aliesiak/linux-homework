#!/usr/bin/env python3
s = input("Строка: ")
print("Длина:", len(s))
print("Первый:", s[0])
print("Последний:", s[-1])
print("Средний:", s[len(s) //2])
print("Каждый второй:", s[::2])
print("Наоборот:", s[::-1])
print("Палиндром:", s == s[::-1])

