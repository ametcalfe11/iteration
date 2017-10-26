# iteration pattern
# doing the same thing once for each member of a list

# [1, 5, 7 ,8 , 4, 3]

def print_list(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	# standard for loop in range
	for i in range (0, len(list)):
		list[i] += 1

	return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern - a type of iteration
# exlclude a calculation from list members

def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"


#accumulation pattern- a type of iteration
# keep track of other data as we go

def sum(numbers):
	total =0
	for n in numbers:
		total += n

	return total


def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max



def average(numbers):
	for n in numbers:
		average=total/n
	return newtotal

def average_minus(numbers):
	for n in numbers:
		averageminus=total/n -2
	return averageminus

# homework: writr a function that finds the average of the scores, 
#write a function that also finds the average, but drops lowest two
