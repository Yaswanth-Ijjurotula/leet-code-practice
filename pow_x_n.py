def myPow(x: float, n: int) -> float:
    res = 1.0
    n2 = n
    if n2 < 0:
        n2 = -1 * n2
    while n2:
        if n2 % 2:
            res = res * x
            n2 = n2 - 1
        else:
            x = x * x
            n2 = n2 // 2
    if n < 0:
        res = 1.0 / res
    return res

if __name__ == "__main__":
    print(myPow(2, 10))