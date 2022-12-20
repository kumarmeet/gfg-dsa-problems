def rearrange(arr):
    if len(arr) % 2 == 0:
        max_ele = len(arr) // 2
        min_ele = len(arr) - max_ele
    else:
        max_ele = len(arr) // 2 + 1
        min_ele = len(arr) - max_ele
    arr[1::2], arr[0::2] = arr[0:min_ele], arr[-1:-max_ele - 1:-1]
    return arr


print(rearrange([1, 2, 3, 4, 5, 6]))

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
