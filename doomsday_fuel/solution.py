import math
import fractions

def solve_vp(p):
    result = [0] * len(p)
    initial_state_vector = [1] * [0]*(len(p)-1)
    """
    Initial state vector is alowas 1, 0, 0, 0, ..., 0,
    so we only need to do the first iteration?
    """
    
def gcdconv(frac, d):
    pass

def m_to_p(m):
    """Converts n->%"""
    def lcm(a, b):
        return (a * b) // fractions.gcd(a, b)

    p = [ [0]*len(m) ] * len(m)
    d = reduce(lcm, [sum(row) if sum(row) is not 0 else 1 for row in m])
    print("\033[31mD={}\033[0m".format(d))
    for r, row in enumerate(m):
        print(">> {}".format(row))
        n = sum(row)
        for c, col in enumerate(row):
            if n > 0:
                p[r][c] = m[r][c] * (d / n)
                print("(%d, %d) = %d" % (r,c, p[r][c]))
    return p, d

def answer(m):
    p, d = m_to_p(m)
    t = solve_vp(p)
    
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
