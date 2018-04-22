# 2018-4-21

from util.time import timedcall

def Fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return Fibonacci(n-1) + Fibonacci(n-2)

print(timedcall(Fibonacci, 4))

