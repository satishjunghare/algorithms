def binarySearch(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        print('mid :%d' % mid)

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, left, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, right, x)
    else:
        return -1

# Inputs
arr = [2,4,6,9,10,16,21,26,27,29,33,35]
x = 6

result = binarySearch(arr, 0, len(arr)-1, x)
print(result)