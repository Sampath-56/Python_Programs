
"""
Input:

A list of integers which may contain zeroes. For the provided example, the input list is [1, 0, 2, 3, 0, 4, 5].

Output:

The list after the algorithm has been applied to all items. For the given example, the output list is [1, 2, 3, 4, 5, 0, 0]"""

list = [1,0,2,3,0,4,5]
for item in list:
    list.remove(0)
    list.append(0)
    print(item)


# Output: 1, 2, 3, 4, 5, 0, 0    