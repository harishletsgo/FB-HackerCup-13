import sys
import math
from collections import Counter
import re
 
in_file = open("find_the_mintxt.txt","r")
exp = in_file.read()
in_file.close()
cases=in_file.split("\n")
def split(line1,line2):
	#inputFile= map(int,exp.split())
	# print inputFile
	#t=inputFile[0]
	n,k=map(int,line1.split())
	a,b,c,r =map(int,line2.split())
	print t
for ind,case in enumerate(xrange(1,len(cases),2)):
	print func(cases[case],cases[case+1])  
