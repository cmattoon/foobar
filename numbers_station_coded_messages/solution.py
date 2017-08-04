"""
Given a non-empty list of positive integers l and a target positive integer t, write a function answer(l, t) which verifies if there is at least one consecutive sequence of positive integers within the list l (i.e. a contiguous sub-list) that can be summed up to the given target positive integer t (the key) and returns the lexicographically smallest list containing the smallest start and end indexes where this sequence can be found, or returns the array [-1, -1] in the case that there is no such sequence (to throw off Lambda's spies, not all number broadcasts will contain a coded message).

For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, the function answer(l, t) would return the list [0, 2] because the list l contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2, for which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4] and the key t as 15, the function answer(l, t) would return [-1, -1] because there is no sub-list of list l that can be summed up to the given target value t = 15.
"""
def answer(l, t):
    _sum = 0
    result = []
    for i, n in enumerate(l):
        for j in range(i, len(l)):
            _sum += l[j]
            if _sum == t:
                result.append( (i,j) )
        _sum = 0

    if len(result) is 0:
        return [-1, -1]
    return list(result[0])
def old_answer(l, t):
    _sum = 0
    iStart = 0

    if t == 0:
        try:
            i = l.index(0)
        except ValueError:
            i = -1
        return [i,i]

    for i, n in enumerate(l):
        while _sum > t:
            _sum -= l[iStart]
            iStart += 1

        if _sum == t:
            j = iStart if i-1 < iStart else i-1

            try:
                while l[iStart] == 0:
                    iStart += 1

                while l[j] == 0:
                    j += 1

                return [iStart,j]
            except IndexError:
                return [-1, -1]

        _sum += n
    if _sum == t:
        return [iStart, i]
    return [-1, -1]
