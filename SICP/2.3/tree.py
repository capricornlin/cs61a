

"""branches = [] is default """

def tree(root_label, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [root_label] + list(branches)

"""tree[0] = root label of tree """
def label(tree):
	return tree[0]

"""tree[1:] = branches of tree
   tree[1:] => except tree[0]
"""
def branches(tree):
	return tree[1:]

""""1. check if tree are list type or just len(tree) < 1

	2. then check branches of tree is tree , branches[tree] = tree[1:]
	   if branches are also tree, then return True.

	3. leaf is also a tree, len(leaf) = 1.
"""
def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)


def fib_tree(n):
	if n == 0 or n ==1:
		return tree(n)
	else:
		left, right = fib_tree(n-2), fib_tree(n-1)
		fib_n = label(left) + label(right)
		return tree(fib_n,[left, right])


def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		branch_counts = [count_leaves(b) for b in branches(tree)]
		return sum(branch_counts)


""" #"""
def partition_tree(n,m):
	if n == 0:
		return tree(True)
	elif n < 0 or m == 0:
		return tree(False)
	else:
		left = partition_tree(n-m,m)
		right = partition_tree(n,m-1)
		return tree(m,[left,right])

"""#"""
def print_parts(tree, partition=[]):
        if is_leaf(tree):
            if label(tree):
                print(' + '.join(partition))
        else:
            left, right = branches(tree)
            m = str(label(tree))
            print_parts(left, partition + [m])
            print_parts(right, partition)
"""#"""
def right_binarize(tree):
        """Construct a right-branching binary tree."""
        if is_leaf(tree):
            return tree
        if len(tree) > 2:
            tree = [tree[0], tree[1:]]
        return [right_binarize(b) for b in tree]
























