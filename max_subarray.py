def max_subarray(arr):
    cur_sum = max_sum = arr[0]
    start_index = end_index=best_start =0
    for i in range(1,len(arr)):
        if arr[i]>curr_sum + arr[i]:
            best_start=i
            cur_sum=arr[i]
        else:
            cur_sum+=arr[i]
        if cur_sum>max_sum:
            max_sum=cur_sum
            start_index=best_start
            end_index=1
    sub_arr=arr[start_index:end_index+1]
    return max_sum ,start_index,end_index,sub_arr,arr[start_index]
