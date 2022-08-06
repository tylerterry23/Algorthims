# Sliding Window algorithm
# Sources Used:
# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# https://youtu.be/g6TLB_tAaCI

# Time Complexity: O(n)
#   - Reason being each element is visited twice at most

# Space Complexity: O(1)
#   - constant space complexity 
#   - The program doesn't contain any loop, recursive function, or call to any other functions.


# How to Identify 
#   - Linked list, array, string
#   - Find a substring of a certain quality
#   - Analyze a portion of a linear data structure


# Example Problems:
#   - Max sum subarray of size 'K
#   - Longest substring with 'K' distinct characters
#   - String anagrams


# Visualization ([    ] = window): 
#  [1,3,2,6,-1] 4,1,8,2 -> 1 [3,2,6,-1,4] 1,8,2 -> 1,3 [2,6,-1,4,1] 8,2 -> ...


# Sliding Window Pseudocode:
# 1. Find the sum of the first 'K' elements
# 2. Add to counter if the average of sum over k is >= than the threshold
# 3. For the rest of the array
#     - slide window up by 1 element 
#     - Calculate the average of these k elements 
#     - If the k element's average is > the threshold, add to the counter
# 4. Return counter






    








