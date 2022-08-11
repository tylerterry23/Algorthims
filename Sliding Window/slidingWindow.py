# Sliding Window algorithm
# Sources can be found in README.md


# Example:

def maxSum(arr, k):
    # set a variable (n) to the length of the array
    n = len(arr)

    # n has to be greater than k
    if n < k:
        print("Error: n must be greater than k")
        return -1

    # compute the sum of the first window of size k
    windowSum = sum(arr[0:k])
    # ! testing
    print("windowSum: ", windowSum)

    # variable to store the max sum (initialize to the sum of the first window)
    maxSum = windowSum

    # compute the sum of the next window by
    # removing the first element of previous
    # Window and adding last element of 
    # the current window
    for i in range(n - k):
        windowSum = windowSum - arr[i] + arr[i + k]
        # ! testing
        print("windowSum: ", windowSum, "-", arr[i], "+", arr[i + k])
        
        if windowSum > maxSum:
            maxSum = windowSum

    return maxSum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))


    








