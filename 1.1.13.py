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


# Result:
# Fastist Average Slowest
# (3.9999999996709334e-06, 5.246956242509928e-06, 0.00017600000000017602)
# (4.999999999810711e-06, 6.144201844241639e-06, 9.400000000070463e-05)
# (2.9999999995311555e-06, 3.936112176049498e-06, 9.999999999976694e-05)
# (1.999999998503199e-06, 2.60743598876308e-06, 9.599999999920783e-05)	
