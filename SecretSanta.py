import random
import sys
import os

file = open(sys.argv[1], "r")
names = file.read().splitlines()

to = list(names)

random.shuffle(to)
random.shuffle(names)

dirName = "./%s" % sys.argv[2]
os.mkdir(dirName)

for index in range(0, len(names) - 1):
	if names[index] == to[index]:
		temp = to[index] 
		to[index] = to[index + 1]
		to[index + 1] = temp

index = len(names) - 1
if names[index] == to[index]:
	temp = to[index] 
	to[index] = to[0]
	to[0] = temp

for index in range(0, len(names) - 1):
	fname = "%s/%s.txt" % (dirName, names[index])
	contents = "%s, please get a gift for %s" % (names[index], to[index])
	file = open(fname, "w")
	file.write(contents)
	file.close()