import sys
import collections

cases=sys.stdin.readlines()
print cases
def initial_seq(k, a, b, c, r):
    v = a
    for _ in xrange(k):
        yield v
        v = (b * v + c) % r
def func(line1,line2):
	n,k=map(int,line1.split())
	a,b,c,r =map(int,line2.split())
	print find_min(n,k,a,b,c,r)
	
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

for ind,case in enumerate(xrange(1,len(cases),2)):
	ans=func(cases[case],cases[case+1])  