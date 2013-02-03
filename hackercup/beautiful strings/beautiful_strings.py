import string

lines = [line.strip() for line in open('beautiful_stringstxt.txt')]
N = lines[0]
out = ''
table = string.maketrans("", "")
for x in xrange(1, int(N) + 1):
    line = lines[x].lower()
    line = line.translate(table, string.punctuation)
    line = line.replace(' ', '')
    set_line = set(line)
    lst = []
    for j in set_line:
        lst.append(line.count(j))
    lst.sort(reverse=True)
    a = 26
    y = 0
    for j in lst:
        y += a * j
        a -= 1
    out += "Case #" + str(x) + ": " + str(y) + "\n"
with open ('output', 'w') as f: 
    f.write (out)