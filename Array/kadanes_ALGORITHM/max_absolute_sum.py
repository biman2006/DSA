def max_absolute_sum(nums):
    
    max_sum=nums[0]
    res=abs(nums[0])
    min_sum=nums[0]
    for i in range(1,len(nums)):
        
        max_sum=max(max_sum+nums[i], nums[i])
        min_sum=min(min_sum+nums[i],nums[i])
        res=max(res,abs(max_sum),abs(min_sum))
    return res 

if __name__=="__main__":
    nums=[1,2,3,-4,-7,5]
    print(max_absolute_sum(nums))