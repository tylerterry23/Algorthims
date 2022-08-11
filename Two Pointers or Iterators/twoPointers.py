def isPairSum(A, N, X):
  
    # represents first pointer
    i = 0
  
    # represents second pointer
    j = N - 1
  
    while(i < j):
        
        # If we find a pair
        if (A[i] + A[j] == X):
            # return answer
            return True, A[i], A[j]
  
        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif(A[i] + A[j] < X):
            i += 1
  
        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1
        else:
            j -= 1
    return 0
  
# array declaration
arr = [2, 3, 5, 8, 9, 10, 11]
  
# value to search
val = 17
  
print(isPairSum(arr, len(arr), val))
  