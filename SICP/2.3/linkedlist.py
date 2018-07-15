

empty = 'empty'

"""is_link(s[1]) => if s is linked_list ,then s[1] must be linked_list,too"""
def is_link(s):
	return s == empty or (len(s) == 2 and is_link(s[1]))


"""1.check link(first,second) is linked_list or not.
   2.Then return [first,rest]
"""
def link(first, rest):
	assert is_link(rest), "rest musr be a linked list."
	return [first, rest]


def first(s):
	assert is_link(s), "first only applies to linked lists."
	assert s!= empty, "empty linked list has no first element."
	return s[0]

def rest(s):
	assert is_link(s),"rest only appies to linked lists."
	assert s!= empty, "empty linked list has no rest."
	return s[1]

four = link(1,link(2,link(3,link(4, empty))))


def len_link(s):
	length = 0
	while s != empty:
		s, length = rest(s), length + 1
	return length

def getitem_link(s, i):
	while i > 0:
		s, i = rest(s), i - 1
	return first(s)
	



