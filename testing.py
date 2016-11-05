from RandomSanta import randomize
import numpy as nd

n = 10000
elements = 10

def checkCorrect():
	names = list(range(elements))
	to = list(names)

	for i in range(n):
		randomize(names, to)

		for j in range(elements):
			if names[j] == to[j]:
				return False

	return True

def checkRandomFromOrder():

	records = nd.zeros((elements, elements))
	names = list(range(elements))
	to = list(names)

	for i in range(n):
		randomize(names, to)

		for j in range(elements):
			records[names[j]][to[j]] += 1

	for row in records:
		for record in row:
			record = record / elements

	return records

correct = checkCorrect()
if not correct:
	print "incorrect"

randOrderRecords = checkRandomFromOrder()
print randOrderRecords



