def fin(n):
    if n == 1:
        return 1
    else:
        return n + fin(n - 1)


def sum(a, b):

    return a+b

print(sum(2,3))