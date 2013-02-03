import sys
import collections
import re

in_file = open("find_the_mintxt.txt","r")
inputFile=in_file.read()
in_file.close()
cases= inputFile.split("\n")
n=cases[0]
print cases[1],n

