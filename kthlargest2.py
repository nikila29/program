import heapq
def findkthlargest(arr,k):
    arr=[-num for num in arr]
    heapq.heapify(arr)
    for x in range(k):
        d=heapq.heappop(arr)
    return -d
arr=[3,2,11,5,6,4]
while True:
    opt=(input("enter the k value(enter no to break):"))
    if (opt=='no'):
        break
    try:
        k=int(opt)
    except:
        print("invalid option")
        continue
    if k < len(arr):
        print(f"{k} nd largest is{findkthlargest(arr,k)}")
        continue
    else:
        print("index out of range")
