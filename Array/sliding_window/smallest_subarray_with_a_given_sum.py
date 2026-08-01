def smallest_subarray_with_a_given_sum(nums,target):
    low=0
    high=0
    res=float('inf')
    sum=0
    while high<len(nums):
        sum+=nums[high]
        while(sum>=target):
            length=high-low+1
            if res>length:
                res= length 
            sum-=nums[low] 
            low+=1
        high+=1 
    return res if res!=float('inf') else 0

if __name__=="__main__":
    nums=[1,4,3,6,7]
    target=5
    print(smallest_subarray_with_a_given_sum(nums,target))
            
        