import sys
with sys.stdin as i:
    n = int(i.readline())
    for _ in range(n):
        a, b = [int(x) for x in i.readline().split()]
        print(a + b if a != b else 2 * (a + b))