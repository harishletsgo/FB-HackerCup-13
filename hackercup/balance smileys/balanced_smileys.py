import re
lines = [line.strip() for line in open('balanced_smileystxt.txt')]
T = lines[0]
out = ''
for i in xrange(1, int(T) + 1):
    line = lines[i]
    line = re.sub('\((([a-z :]|\([a-z: ]*\)*)|:\)|:\(|)*\)', '', line)
    line = re.sub(':\(|:\)|[a-z ]|:', '', line)
    if line == '':
        out += "Case #" + str(i) + ": YES\n"
    else:
        out += "Case #" + str(i) + ": NO\n"
with open('output', 'w') as f:
    f.write(out)