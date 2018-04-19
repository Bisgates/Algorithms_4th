# 2018-4-18

import random
import sys

num = int(sys.argv[1])

# Read from txt file
with open('sortedList_100k.txt') as reader:
	lis = [int(ele.strip()) for ele in reader]

def binarySearch(lis, num):
	left, right = 0, len(lis)-1
	
	iters = 0
	while left <= right:
		iters += 1
		mid = int((left + right)/2)
		if lis[mid] == num:
			print('\nFind it! %d is in the list. %d iters, %.0f times faster.' % (num, iters, mid/iters))
			return True
		elif lis[mid] < num:
			left = mid + 1
		else:
			right = mid - 1
	print('\n%d is not in the list.' % num)
	return False
			
binarySearch(lis, num)

print('\n************ TEST ***************')
assert binarySearch(lis, max(lis)) == True
assert binarySearch(lis, min(lis)) == True

num = random.choice(lis)
assert binarySearch(lis, num) == True

num = random.choice(lis)
assert binarySearch(lis, num) == True


