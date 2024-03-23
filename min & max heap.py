def is_min_heap (arr):
    n=len(arr)
    for i in range(n//2):
        left_child=2*i+1
        right_child=2*i+2
        if left_child<n and arr[left_child]<arr[i]:
            return False
        if right_child<n and arr[right_child]<arr[i]:
            return False
    return True
def is_max_heap(arr):
    n=len(arr)
    for i in range (n//2):
        left_child=2*p+1
        right_child=2*p+2
        if left_child <n and arr[left_child]>arr[i]:
            return False
        if right_child < n and arr[right_child]>arr[i]:
            return False
    return True
min_heap_list=[21,3,6,5,9,8,10]
if is_min_heap(min_heap_list):
    print(min_heap_list)
    print("is_min_heap:",is_min_heap(min_heap_list))
else:
    print(min_heap_list)
    print("no heap")
