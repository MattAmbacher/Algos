import random

def counting_sort(A, k):
	'''
	Input: Sequence A containing elements in the range 0 to k, integer k where k is the maximum value in A.
	Output: Sorted sequence B

	Sorts in O(n) time and 3n space
	'''
	n = len(A)
	B = [0 for n in A]
	C = [0 for n in range(k+1)]
	for j in range(n):
		C[A[j]] += 1
	#C[i] now contains the number of elements in A equal to i	
	for i in range(1,k+1):
		C[i] += C[i-1] 
	C = [n-1 for n in C]
	#C[i] now contains the number of elements in A less than or equal to i
	#Do the sorting into B
	for j in range(n-1, -1, -1):
		B[C[A[j]]] = A[j]
		C[A[j]] -= 1 #if there are duplicates in A, this puts the duplicate(s) in the position before A[j]
	return B


if __name__ == '__main__':
	A = [2, 5, 3, 0, 2, 3, 0, 3] 
	k = max(A)
	print(counting_sort(A,k))

