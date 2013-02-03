import re
splitter = re.compile(r'\d+')
match1 = splitter.findall("GoTo: 7018 6453 12654\n")
print match1