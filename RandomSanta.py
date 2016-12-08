import random

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
