def answer(l):
    l.sort(key=lambda i: [int(n) for n in i.split('.')])
    return l
