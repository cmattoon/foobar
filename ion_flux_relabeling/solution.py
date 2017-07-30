#!/usr/bin/env python


def answer(h, q):
    if h is 0: return -1
    root = pow(2, h)-1

    def _search(height, value, parent):
        L, R = parent-pow(2, height-1), parent-1

        if value in [L, R]:
            return parent

        if value < L:
            return _search(height-1, value, L)

        return _search(height-1, value, R)

    return map(lambda el: -1 if el >= root else _search(h, el, root), q)
