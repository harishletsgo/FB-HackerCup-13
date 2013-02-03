import sys
cases=sys.stdin.readlines()
def func(line1,line2):
    n,k=map(int,line1.split())
    a,b,c,r =map(int,line2.split())
    m=[None]*n                       #initialize
    m[0]=a                  
    for i in xrange(1,k):            #same as above          
        m[i]= (b * m[i - 1] + c) % r
    temp={}
    for x in m[0:k]:                   
        temp[x]=temp.get(x,0)+1       

    i=-1
    while True:
            i+=1
            if i not in temp:
                m[k]=i          #set the value of m[k]
                break
    for j in range(1,n-k):      #now set the values of m[k+1] to m[n-1]
        i=-1
        temp[m[j-1]] -= 1       #decrement it's value, as it is now out of K items
        temp[m[k+j-1]]=temp.get(m[k+j-1],0)+1   # new item added to the current K-1 items

        while True:
            i+=1
            if i not in temp or temp[i]==0:  #if i not found in dict or it's val is 0
                m[k+j]=i                     
                break

    return m[-1]

for ind,case in enumerate(xrange(1,len(cases),2)):
    ans=func(cases[case],cases[case+1])
    print "Case #{0}: {1}".format(ind+1,ans) 