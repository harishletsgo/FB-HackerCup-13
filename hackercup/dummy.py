import collections

def initial_seq(k, a, b, c, r):
    v = a
    for _ in xrange(k):
        yield v
        v = (b * v + c) % r

def find_min(n, k, a, b, c, r):
    m = [0] * (2 * k + 1)
    for i, v in enumerate(initial_seq(k, a, b, c, r)):
        m[i] = v
    ks = range(k+1)
    s = collections.Counter(m[:k])
    for i in xrange(k, len(m)):
        m[i] = next(j for j in ks if not s[j])
        ks.remove(m[i])
        s[m[i-k]] -= 1
    return m[k + (n - k - 1) % (k + 1)]


print find_min(97, 39, 34, 37, 656, 97)
print find_min(186, 75, 68, 16, 539, 186)
print find_min(137, 49, 48, 17, 461, 137)
print find_min(1000000000, 100000,1, 1, 0, 2)