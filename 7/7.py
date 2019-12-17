import sys
with sys.stdin as i:
    n = int(i.readline())
    for _ in range(n):
        count = int(i.readline())
        lst = [float(i.readline()) for __ in range(count)]
        min_, max_ = min(lst), max(lst)

        print('\n'.join([str(round((x - min_) / (max_ - min_) * 255)) for x in lst]))