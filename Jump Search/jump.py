import math

def jumpSearch(arr, x, n):
    
    # Find the block size to be jumped
    step = math.sqrt(n)
    
    # Finding the block where element is present
    prev = 0
    while arr[int(min(step, n)-1)] < 1000:
        prev = step
        step += math.sqrt(n)
        # print('n : %d | prev : %d | step : %d' % (n, prev, step))
        if prev >= n:
            return -1

    # Doing a linear search for x in block beginning with prev
    print('n : %d | prev : %d | step : %d' % (n, prev, step))
    while arr[int(prev)] < x:
        prev += 1
        print(min(step, n))
        if prev == min(step, n):
            return -1
    
    if arr[int(prev)] == x:
        return prev
    
    return -1

# Inputs
arr = [
    0, 1, 1, 2, 3, 
    5, 8, 13, 21, 34, 
    55, 89, 144, 233, 377, 
    610, 720, 850, 960, 968, 
    980, 990, 992, 1000, 1120]
x = 992
n = len(arr)

# Find the index of 'x' using jump search
searchIndex = jumpSearch(arr, x, n)
print(searchIndex)
# Print the index
# print(searchIndex)