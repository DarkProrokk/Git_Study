def fin(n):
    if n == 1:
        return 1
    else:
        return n + fin(n - 1)


