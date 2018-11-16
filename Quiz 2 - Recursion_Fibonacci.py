def get_fib(position):
	if postion == 0:
		return 0
	elif position == 1:
		return 1
	else:
		return get_fib(position-1) + get_fib(position-2)

def get_fib(position):
	if position == 0:
		return 0
	elif position == 1:
		return 1
	else:
		return get_fib(position-1) + get_fib(position-2)

def get_fib(position):
	if postion == 0:
		return 0
	elif position == 1:
		return 1
	else:
		return get_fib(positon-1) + get_fib(position-2)

def get_fib(position):
	if position == 0:
		return 0
	elif position == 1:
		return 1
	else:
		return get_fib(position-1) + get_fib(position-2)
		
#Iterative Approach - return first n fibonacci numbers:
def get_fib(n):
	if n == 0:
		return []
	elif n == 1:
		return [0]
	elif n == 2:
		return [0, 1]
	else:
		l = [0, 1]
		first = l[0]
		second = l[1]
		while len(l) < n:
			third = first + second
			l.append(third)
			first = second 
			second = third
		return l or l[len(n)-1] #depending on whether you just want the nth number or all the numbers!




