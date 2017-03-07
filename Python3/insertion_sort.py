def insertion_sort(A):
	'''
	input: sequence A = [a_1, a_2, a_3,...,a_n]
	output: sequence A' = [a_1', a_2', a_3', ... , a_n'] where a_1' < a_2' < a_3' < ... < a_n'
	'''
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		while i >=0 and key < A[i]:
			A[i+1] = A[i] # move each entry to the right one place if A[j] is less than A[i]
			i -= 1
		A[i+1] = key
	return A

#testing with a small list
if __name__ == '__main__':
	A = [5, 2, 1, 6, 3, 4]
	print('A is: {} originally'.format(A))
	print('Sorting...')
	sorted_A = insertion_sort(A)
	print('A is now: {}'.format(sorted_A))
	
