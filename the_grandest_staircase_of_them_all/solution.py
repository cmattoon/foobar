import math


def answer(n):
    
    MEMO = {}

    def step(bricks, last):
        try:
            return MEMO[(bricks, last)]
        except KeyError:
            pass

        if bricks is 0: return 1

        start = int(math.ceil((-1 + math.sqrt( 1 + 8*bricks) ) / 2))
        end = int(bricks) if last is -1 else last
        end = min(end, bricks+1)

        n = 0
        for i in range(start, end):
            #print(i, n)
            n += step(bricks-i, i)
        #print(n)
        MEMO[(bricks, last)] = n
        return n

    return step(n, -1)
