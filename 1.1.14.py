# 2018-4-21

import math
from util.time import timedcalls

def lg(N, base=2):
	"return the largest int not larger than the log of N "
	ans = 0
	while N >= base:
		N /= base
		ans += 1
	return ans

def lg_math(N, base=2):
	return int(math.log(i, base))

#------------TEST---------------

for i in range(1, 10000):
	assert lg_math(i) == lg(i)

print('Passed all test cases!')

print(timedcalls(5., lg, 456789))
print(timedcalls(5., lg_math, 456789))


# two-times slower than build in function
# (2.9999999995311555e-06, 4.227507353743107e-06, 0.0001129999999998077)
# (9.999999974752427e-07, 2.145140613938827e-06, 0.00011800000000050659)
