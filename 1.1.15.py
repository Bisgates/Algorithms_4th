# 2018-4-21

def histogram(A, m):
	his = [0]*m
	for ele in A:
		his[ele] += 1
	return his







#--------------------TEST------------------

assert histogram([1,1,1,6,3,3], 7) == [0, 3, 0, 2, 0, 0, 1]


print('Passed all test cases!')	
	
