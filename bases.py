#!/usr/bin/env python3
import sys
n = int(sys.argv[1])
b, o, h = bin(n), oct(n), hex(n)
print(b, o, h)
print(int(b, 2), int(o, 8), int(h, 16))

