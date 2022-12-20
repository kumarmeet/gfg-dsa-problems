def majority_wins(arr, x, y):
    a = arr.count(x)
    b = arr.count(y)

    return min(x, y) if a == b else x if a > b else y


print(majority_wins([40, 85, 9, 14, 13], 13, 32))

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
