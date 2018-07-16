

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
	

def len_link_recursive(s):
	if s == empty:
		return 0
	return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
	if i == 0:
		return first(s)
	return getitem_link_recursive(rest(s),i - 1)

""" 1. simple way to try recursion len_link_recursive and getitem_link_recursive 
	2. Because rst(s) return s[1], the last sequence's element(s[1]) will be 'empty'.
	3. So we can get the length. 
"""
empty = 'empty'

def first(s):
       return s[0]
def rest(s):
       return s[1]
       

   
four = [1, [2, [3, [4, 'empty']]]]

def len_link_recursive(s):
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s),i - 1)
    
    
len_link_recursive(four)


""" # """
def extend_link(s,t):
	assert is_link(s) and is_link(t)
	if s == empty:
		return t
	else:
		return link(first(s),extend_link(rest(s),t))


""" # """
def apply_to_all_link(f, s):
	assert is_link(s)
	if s == empty:
		return s
	else:
		return link(f(first(s)),apply_to_all_link(f,rest(s)))

""" # """
def keep_if_link(f,s):
	assert is_link(s)
	if s == empty:
		return s
	else:
		kept = keep_if_link(f, rest(s))
		if f(first(s)):
			return link(first(s), kept)
		else:
			return kept

""" # """
def join_link(s, separator):
	if s == empty:
		return ""
	elif rest(s) == empty:
		return str(first(s))
	else:
		return str(first(s)) + separator + join_link(rest(s), separator)

""" # """
def partitions(n,m):

	if n == 0:
		return link(empty, empty)
	elif n < 0 or m == 0:
		return empty
	else:
		using_m = partitions(n-m, m)
		with_m = apply_to_all_link(lambda s: link(m, s), using_m)
		without_m = partitions(n, m-1)
		return extend_link(with_m, without_m)

""" # """
def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))












		

			
		


































