import sys
with sys.stdin as i:
    n = int(i.readline())
    for _ in range(n):
        print(i.readline()[:-1].lower())