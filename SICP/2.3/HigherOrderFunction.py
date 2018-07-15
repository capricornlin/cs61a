



from operator import mul 
from operator import add


def apply_to_all(map_fn,s):
	return [map_fn(x) for x in s]

def keep_if(filter_fn,s):
	return [x for x in s if filter_fn(x)]


def reduce(reduce_fn,s,initial):
	"""	
		redued value changed every x in s
	   	=> reduced = reduce_fn(reduced,x)

	"""
	reduced = initial
	for x in s:
		reduced = reduce_fn(reduced,x)
	return reduced


"""keep_if(lambda x : 12 % x == 0,range(2,12))

	"""
def divisors_of(n):
	divides_n = lambda x : n % x == 0
	return [1] + keep_if(divides_n, range(2,n))



""" sum_of_divisors(n) => add all divisors together
	=> sum_of_divisors(12) = 1 + 2 + 3 + 4 + 6
"""
def sum_of_divisors(n):
	return reduce(add,divisors_of(n),0)


""" perfect(n) => add all divisors together equal n himself """ 

def perfect(n):
	return sum_of_divisors(n) == n

city = 'Berkeley'

digits = [1, 8, 2, 8]








