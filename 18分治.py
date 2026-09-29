def mypow(x, n):
    if n < 0:
        return 1/mypow(x, -n)

    if n == 0:
        return 1

    if n % 2 == 0:
        half = mypow(x, n // 2)
        return half * half

    else:
        half = mypow(x, n // 2)
        return x * half * half

print(mypow(2.0, 10))
print(mypow(2.0, -2))
print(mypow(2.0, 0))


'''优化'''
def mypow(x, n):
    if n < 0:
        return 1 / mypow(x, -n)
    if n == 0:
        return 1
    half = mypow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half