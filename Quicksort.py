def partition(A,left_index,right_index):
    pivot = A[left_index]
    i = left_index + 1
    for j in range(left_index + 1,right_index):
        if(A[j] < pivot):
            A[j],A[i] = A[i],A[j]
            i+=1
    A[left_index],A[i-1] = A[i-1],A[left_index]
    return i-1,right_index-left_index

def choose_pivot(A):
    return A[0]

def quicksort(A,begining,end):
    print(begining)
    print(end)
    if(begining < end):
        pivot_index = begining
        left,right = partition(A,pivot_index,end)
        quicksort(A,begining,left)
        quicksort(A,right,end)

test_array = [3,5,9,0,1,6,7,4]
quicksort(test_array,0,len(test_array)-1)
print(test_array)
