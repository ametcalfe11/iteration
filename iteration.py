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
	total=0
	count=len(numbers)
	for n in numbers:
		total +=n
		average= total/count
	return average



def average_minus(numbers):
	total=0
	count=len(numbers)
	for n in numbers:
		total +=n
		average= total/count


	current_min = numbers[0]
	for n in numbers:
		if n < current_min:
			current_min = n

	current_min2 = numbers[0]
	for n in numbers:
		if n <= current_min:
			current_min2 = n

	averageminus= total/count- current_min-current_min2
	return averageminus



def alternating_sum (numbers):
	total=0
	for i in range(0, len (numbers)):
		if i%2==0:
			total += numbers[i]
		else:
			total-= numbers[i]
	return total


def sum_outside (numbers):
	total=0
	for n in numbers:
		if not (min <= n and n < max):
			total +=n
	return total	


def count_close_remainders (numbers):
	count=0
	for n in numbers:
		remainder = n% divisor
		if remainder <= 1 or remainder == divisor-1:
			count +=

def double_down(numbers, target):
	result = [maybe_doubled(numbers[0], numbers[0],target)]
	for i in range (1, len(numbers)):
		result.append[maybe_doubled(numbers[0], numbers[0]. target)]	
	return result

def maybe_doubled(n, prev_n, target):
		distance=abs(n-target)
		if n < prev_n or distance <=3:
			return 2*n
		return n

