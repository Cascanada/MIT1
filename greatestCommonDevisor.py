#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens


def iGcd(m, n):
    """Calculate the Greatest Common Divisor of m and n.

    Unless n==0, the result will have the same sign as n (so that when
    n is divided by it, the result comes out positive).
    """
    while n > 0:
        m, n = n, m % n
    return m


# This procedure recursively computes the gcd of two numbers
def rGcd(m, n):
    print (m, n)
    if m % n == 0:
        return n
    else:
        gcd = rGcd(n, m % n)
        return gcd

# Marc Test: The return n goes back to different n values as we get out of the recursive calls.
def rGcdMarc(m, n):
    # print (m, n)
    if m % n == 0:
        return n
    else:
        return rGcdMarc(n, m % n)


# iGcd(120,8)

# rGcd(120,32)

print(rGcdMarc(120, 32))
