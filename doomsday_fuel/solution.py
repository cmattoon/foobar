import math
import fractions


def im(n):
    """initmatrix"""
    return [[0 for i in range(n)] for i in range(n)]

def idmatrix(n):
    """Returns an identity matrix of size N
    """
    m = im(n)
    for i in range(n):
        m[i][i] = 1
    return m

def msort(m):
    """
    Sorts a matrix into ___?
    """
    pass

def iterm(m):
    lr = len(m)
    lc = len(m[0])
    for r in xrange(lr):
        for c in xrange(lc):
            yield r, c, m[r][c]

def add_absorbing_states(m):
    """
    A terminal state is represented by 'sum(row) is 0'

    Replace these with P(i)=1
    
    Do I necessarily want this? 
    """
    for r, c, v in iterm(m):
        if sum(m[r]) is 0:
            m[r][r] = 1
    return m

def msub(a, b):
    """a - b"""
    m = im(len(a))
    for r, c, v in iterm(m):
        m[r][c] = a[r][c] - b[r][c]
    return m

def partition(m):
    """Return I, O, R, Q
    """
    pass

def invertm(m):
    """Invert m"""
    pass

def get_f(m):
    """
    Returns F for F = (I-Q)^-1
    """
    I = idmatrix(len(m))
    Q = get_Q(m)
    return invertm(msub(I-Q))

def answer(m):
    pass

if __name__ == '__main__':

    
    m=[
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    m2=[
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    for row in m:
        print("\033[33m{}\033[0m".format(row))
        P,d= m_to_p(m)
        
    for row in P:
        print("\033[32m{}\033[0m".format(row))
            
