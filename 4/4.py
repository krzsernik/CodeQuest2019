import sys
with sys.stdin as i:
    n = int(i.readline())
    for _ in range(n):
        v, b = i.readline().split()
        v = int(v)
        b = b == "true"

        if b:
            v -= 5

        if v <= 60:
            print("no ticket")
        elif v <= 80:
            print("small ticket")
        else:
            print("big ticket")