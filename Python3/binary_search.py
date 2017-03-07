def binary_search(A, val, low, high):
	'''
	Input: Sorted sequence A, desired value to low/high refer to the section of A we check
	Output: index of val in A. returns -1 if val not in A
	'''
	if low > high:
		return -1
	mid = (low + high)//2
	if A[mid] == val:
		return mid
	elif A[mid] > val: #val is in lower half
		return binary_search(A, val, low, mid-1)
	else: 		   #val is in upper half
		return binary_search(A,val,mid+1,high)


#test
if __name__ == '__main__':
	A = [n for n in range(1,int(1e3))]
	print(A)
	ind = binary_search(A, 5000, 0, len(A)-1)
	print(ind)
	if ind != -1:
		print(A[ind])
