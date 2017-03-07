import random 

def merge_sort(A):
	'''
	Input: sequence of numbers [a_1, a_2, a_3, ... , a_n]
	Output: sequence of numbers [a_1', a_2', a_3', ... , a_n'] such that a_1' < a_2' < a_3' < ... < a_n'
	'''
	n = len(A)
	if n == 1: return A
	left = merge_sort(A[:int(n/2)])
	right = merge_sort(A[int(n/2):])
	return merge(left, right)

def merge(A,B):
	'''
	Merges two sequences of sorted numbers into one sequence
	'''
	n1 = len(A)
	n2 = len(B)
	C = []
	i, j = (0,0) #i keeps track of A, j keeps track of B
	for n in range(n1+n2):
		if i >= len(A): 
			#We're out of elements in A
			C.extend(B[j:])
			return C

		if j >= len(B):
			#We're out of elements in B
			C.extend(A[i:])
			return C

		if A[i] < B[j]:
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1
	return C

if __name__ == '__main__':
	A = [n for n in range(int(10e4))]
	random.shuffle(A)
	print(A)
	print('sorting...')
	print(merge_sort(A))
