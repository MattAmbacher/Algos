def quicksort(A, p, q):
    '''
    Hoare 1962 algorithm for quicksorting in O(nlgn) time and O(n) space
    Input: 
            Sequence of numbers A, lower index p, upper index q
            First call to quicksort should have p = 0, q = len(A) - 1
    Output:
            Sorted list A
    '''
    if p < q: 
        i = partition(A, p, q) #gives index of pivot
        quicksort(A, p, i-1)
        quicksort(A, i+1, q)

def partition(A, p, q):
    '''
    Workhorse of quicksort. Partitions the list A into two sublists,
    the first containing elements leq to pivot x, second containing
    elements gt pivot x
    
    Returns index of pivot
    '''
    x = A[p] #sets the pivot element
    i = p
    for j in range(p+1,len(A)):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j] #swap jth element with one past pivot, new pivot is now i <- i +1
    A[p], A[i] = A[i], A[p] #swap pivot and the index that splits the array
    return i

if __name__ == '__main__':
    A1 = [5, 3, 16, 8, 3, 1, 10, 7] #even
    quicksort(A1, 0, len(A1)-1)
    A2 = A1
    A2.append(9) #odd
    quicksort(A2, 0, len(A2)-1)

    print(A1)
    print(A2)
