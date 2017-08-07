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

def m2p(matrix):
    """


    """
    for r, row in enumerate(matrix):
        if sum(row) is 0:
            # Absorbing states have p=1.0
            matrix[r][r] = 1
    return matrix

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
            
