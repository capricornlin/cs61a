

"""get divisors from an integer n"""
def divisors(n):
	return[1] + [x for x in range(2,n) if n % x == 0]


"""get width"""
def width(area, height):
	assert area % height == 0
	return area // height


"""get perimeter from an given area"""
def perimeter(width, height):
	return 2 * width + 2 * height




def minimum_perimeter(area):
	"""get a list of heights from a given area""" 
	heights = divisors(area)

	"""heights is a list.
	   perimeters are a list, get perimeter from given heights list.
	"""

	perimeters = [perimeter(width(area, h),h) for h in heights]
	return min(perimeters)

	"""[minimum_perimeter(n) for n in range(1,10)]
		n in range(1,10) is a given area.
		and we have mutiple heights, width possible in this given area.
		so the minimum_perimeter(n) is to get a minimum_perimeters of 
		this possible heights and width.
	"""


