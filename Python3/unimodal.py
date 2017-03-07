def unimodal(A):
	'''
	A sequence is unimodal if for 1 <= i < m, A[i] < A[i+1] and 
	for m <= i <= n, A[i] > A[i+1].

	This finds the maximum of a unimodal array in log(n) time
	'''
	n = len(A)
	mid = n//2
	if mid == 0:
		return A[mid]

	if A[mid] > A[mid-1]:
		return unimodal(A[mid:])
	else:
		return unimodal(A[:mid])

if __name__ == '__main__':
	A = [1 ,2, 3, 4, 5, 6, 7, 6, 5, 4, 3] #odd n
	print(unimodal(A)) 
	A.append(2) #even n
	print(unimodal(A))
