import heapq
def findKthLargest(arr,k):
    arr=[-num for num in arr]
    heapq.heapify(arr)
    for x in range(k):
        d=heapq.heappop(arr)
    return -d
arr=[3,2,1,5,6,4]
k=2
print (f" {k} th nd largest is {findKthLargest(arr,k)}")
        
