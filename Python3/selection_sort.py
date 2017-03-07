def selection_sort(A):
	'''
	input: sequence of numbers [a_1, a_2, a_3, ... , a_n]
	output: sequence of numbers [a_1', a_2', a_3', ... , a_n'] where a_1' < a_2' < a_3' < ... < a_n'
	'''
	for j in range(len(A)-1):
		key = A[j]
		index = j
		for i in range(j+1,len(A)):
			if key > A[i]:
				index = i
				key = A[i]
		A[index] = A[j]
		A[j] = key
	return A

#testing
if __name__ == '__main__':
	A = [5,2,4,6,1,3]
	selection_sort(A)
