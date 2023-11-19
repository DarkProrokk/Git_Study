def fin(n):
    if n == 1:
        return 1
    else:
        return n + fin(n - 1)


def sum(a, b):
    return a+b

def raz(a, b):
    return a-b


print(raz(8, 5))