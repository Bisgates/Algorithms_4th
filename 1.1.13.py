# 2018-4-21
# Transpose a Matrix

from util.time import timedcall, timedcalls
import numpy as np

def transpose_1(A):
	ii, jj = len(A), len(A[0])
	B = [[0]*ii]*jj
	for i in range(ii):
		for j in range(jj):
			B[j][i] = A[i][j]
	return B


def transpose_2(A):
	ii, jj = len(A), len(A[0])
	B = [[A[i][j] for j in range(jj)] for i in range(ii)]
	return B

def transpose_3(A):
	"Return A.transpose"
	return [list(x) for x in zip(*A)]


def transpose_4(A):
	"Test Numpy transpose speed"
	return np.transpose(A)


#---------------------TEST------------------------
A = [[1,2,3,4,5], [2,3,4,5,6],[3,4,5,6,7]]


print(timedcalls(5., transpose_1, A))

print(timedcalls(5., transpose_2, A))

print(timedcalls(5., transpose_3, A))

A_np = np.array(A)
print(timedcalls(5., transpose_4, A_np))





	
	
