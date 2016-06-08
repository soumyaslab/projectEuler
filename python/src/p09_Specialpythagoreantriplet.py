

from math import sqrt
L = 1000    # Pythagorian sums are always even

def p_trip(ps):
    for m in range(int(sqrt(ps/2)), int(sqrt(ps)/2), -1):
        n = ps / (2.0*m) - m    # the '2.0' forces floating point math
        print "ps: %d, m: %d, n: %d " % (ps,m,n)
        if n > 0 and n % 1 == 0:
            print "ps: %d, m: %d, n: %d " % (ps,m,n)
            a, b, c = m*m - n*n, 2*m*n, m*m + n*n
            return  map(int, (a, b, c, a*b*c))    # convert to integers
        print "**************************************\n"

a, b, c, p = p_trip(L)
print a, '+', b, '+', c, '=', L, 'product abc =', p