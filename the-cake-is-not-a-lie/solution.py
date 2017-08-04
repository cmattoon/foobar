def answer(s):
    L = len(s)
    for i in range(L):
        sub = s[:i]
        l = len(sub)
        occurs = s.count(sub)
        if occurs * l == L:
            return occurs
    return 1
