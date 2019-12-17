import sys
import math

def calc(height):
    earth_d = 40075. / math.pi
    x_d = earth_d + height * 2

    return round(x_d * math.pi * 10) / 10

with sys.stdin as i:
    n = int(i.readline())

    for _ in range(n):
        height = float(i.readline())

        print(calc(height))