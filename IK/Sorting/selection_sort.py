"""Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n)2).
* Auxiliary space: O(1).
* Total space: O(n).
"""

def selection_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    arrlength = len(arr)
    for i in range(arrlength):
        minindex = i
        for j in range(i+1,arrlength):
            if arr[j] < arr[minindex]:
                minindex = j
        (arr[i],arr[minindex]) = (arr[minindex],arr[i])
    return arr

arr = [5,8,3,9,4,1,7]
result = selection_sort(arr)
print (result)