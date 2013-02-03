import sys, os
import collections

def min(str1, str2):
    para1 = str1.split()
    para2 = str2.split()

    n = int(para1[0])
    k = int(para1[1])
    a = int(para2[0])
    b = int(para2[1])
    c = int(para2[2])
    r = int(para2[3])

    m = [0] * (2*k+1)
    m[0] = a

    s = collections.Counter()

    s[a] += 1
    rs = {}
    for i in range(k+1):
        rs[i] = 1

    for i in xrange(1,k):
        v = (b * m[i - 1] + c) % r
        m[i] = v
        s[v] += 1
        if v < k:
            if v in rs:
                rs[v] -= 1
                if rs[v] == 0:
                    del rs[v]

    for j in xrange(0,k+1):
        for t in rs:
            if not s[t]:
                m[k+j] = t
                if m[j] < k:
                    if m[j] in rs:
                        rs[m[j]] += 1
                    else:
                        rs[m[j]] = 0

                rs[t] -= 1
                if rs[t] == 0:
                    del rs[t]

                s[t] = 1
                break

        s[m[j]] -= 1

    return m[k + ((n-k-1)%(k+1))]

if __name__=='__main__':
    lines = []
    user_input = raw_input()
    num = int(user_input)

    for i in xrange(num):
        input1 = raw_input()
        input2 = raw_input()
        print "Case #%s: %s"%(i+1, min(input1, input2))