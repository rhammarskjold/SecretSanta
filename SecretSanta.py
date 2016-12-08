import sys
import os

from RandomSanta import randomize

def main(namesFile, dirName):
	file = open(namesFile, "r")
	names = file.read().splitlines()

	os.mkdir(dirName)

	to = list(names)
	randomize(names, to)

	for index in range(0, len(names)):
		fname = "%s/%s.txt" % (dirName, names[index])
		contents = "%s, please get a gift for %s" % (names[index], to[index])
		file = open(fname, "w")
		file.write(contents)
		file.close()

main(sys.argv[1], sys.argv[2])