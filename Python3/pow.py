def pow(x, n):
	'''
	Computes the n^th power of x
	'''
	if n == 2:
		return x * x
	if n % 2 == 0:
		return pow(x, n/2) * pow(x, n/2)
	else:
		return x * pow(x, (n-1)/2) * pow(x, (n-1)/2)


if __name__ == '__main__':
	print(pow(2,4)) #output 16
	print(pow(2,5)) #output 32
