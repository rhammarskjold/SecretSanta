import random
import sys
import os

#randomizes such that names[i] != to[i] for any i
def randomize(names, to):
	
	random.shuffle(to)
	random.shuffle(names)

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


def main():
	file = open(sys.argv[1], "r")
	names = file.read().splitlines()


	dirName = "%s" % sys.argv[2]
	os.mkdir(dirName)

	to = list(names)
	randomize(names, to)

	for index in range(0, len(names) - 1):
		fname = "%s/%s.txt" % (dirName, names[index])
		contents = "%s, please get a gift for %s" % (names[index], to[index])
		file = open(fname, "w")
		file.write(contents)
		file.close()

main()