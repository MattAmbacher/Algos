from merge_sort import merge_sort
from binary_search import binary_search

def pair_sum(S, val):
	'''
	This is a solution to 2.3-7 in Cormen's Introduction to Algorithms.
	Describe a theta (n lg n)-time algorithm that, given a set S of n integers and another integer x,
	determins whether or not there exist two elements in S whose sum is exactly x.
	'''

	#First sort the list in (n lg n) time
	A = merge_sort(S)
	for j in range(len(A)-1): #iterate through each element ( theta(n) time)
		match = binary_search(A, val - A[j], j+1, len(A)-1) #if i + j = val, then val - j = i. We look for this i.
		if match != -1:
			return True
	return False

if __name__ == '__main__':
	S1 = [7, 1, 1, 1, 7]
	print(pair_sum(S1, 14)) #should print true
	S2 = [1,2,3,4,5,6]
	print(pair_sum(S2, 14)) #should print false
