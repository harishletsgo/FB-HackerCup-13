from collections import deque

def get_next(i):
    while i in set_last_k:
        i += 1
    return i

for line1, line2 in zip(cases[1::2], cases[2::2]):
    n, k = map(int, line1.split())
    a, b, c, r = map(int, line2.split())
    m = [a]
    for i in xrange(k - 1):
        m.append((b * m[-1] + c) % r)
    last_k = deque(m)
    set_last_k = set(last_k)
    next = get_next(0)
    for j in xrange(min(k, n - k)): # original list - may contain duplicates
        i = next
        removed = last_k.popleft()
        if removed in last_k:
            next = get_next(i+1)
        else:
            set_last_k.remove(removed)
            if removed < i:
                next = removed
            else:
                next = get_next(i+1)
        m.append(i)
        last_k.append(i)
        set_last_k.add(i)
    if n > 2*k:
        for j in xrange(n - 2*k): # extended list - no duplicates
            i = next
            removed = last_k.popleft()
            set_last_k.remove(removed)
            if removed < i:
                next = removed
            else:
                next = get_next(i + 1)
            m.append(i)
            last_k.append(i)
            set_last_k.add(i)
    print len(m), m[-1]