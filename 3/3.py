import sys
with sys.stdin as i:
    n = int(i.readline())
    for _ in range(n):
        a, b = [x == "true" for x in i.readline().split()]
        print(str(a == b).lower())