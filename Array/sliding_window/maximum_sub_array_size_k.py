def maximum_subarray_size_k(nums,k):
    low=0
    high=k-1
    res=0
    sum=0

    for i in range(high+1):
        sum=sum+nums[i]
    
    while(high<len(nums)):
        res=max(res,sum)
        low+=1
        high+=1
        if (high==len(nums)):
            break 
        sum=sum-nums[low-1]
        sum=sum+nums[high]
    return res 

if __name__=="__main__":
    nums = [2, 1, 5, 1, 3, 2]
    k = 3

    print(maximum_subarray_size_k(nums, k))
    