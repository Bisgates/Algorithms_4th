# 2018-4-21

import math

def lg(N, base=2):
	"return the largest int not larger than the log of N "
	ans = 0
	while N >= base:
		N /= base
		ans += 1
	return ans


#------------TEST---------------

for i in range(1, 10000):
	assert int(math.log(i, 2)) == lg(i)

print('Passed all test cases!')
