# 2018-4-19
# Write a code fragment that prints the contents of a two-dimensional boolean array, using * to represent true and a space to represent false. Include row and column numbers.

def printBooleanArray(A):
	for line in A:
		for ele in line:
			if ele:
				print('*', end=''),
			else:
				print(' ', end=''),
		print('')


#----------------TEST-----------------
A = [[True, False, True, True], [True, False, False, False], [False, False, False, True]]
B = [[True], [False]]

printBooleanArray(A)
print('---------')
printBooleanArray(B)
