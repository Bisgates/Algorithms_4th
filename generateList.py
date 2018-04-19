# 2018-4-19

import random

lenth = 1000*1000

left, right = -100, 100000000

lis = sorted([random.randint(left, right) for i in range(lenth)])

for ele in lis:
	print(ele)
