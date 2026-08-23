def circular_subarray_sum(nums):
    
    total_sum=nums[0]

    max_ending=nums[0]
    max_sum=nums[0]

    min_ending=nums[0]
    min_sum=nums[0]

    for i in range (1,len(nums)):
        total_sum+=nums[i]

        max_ending=max(max_ending+nums[i],nums[i])
        max_sum=max(max_ending,max_sum)

        min_ending=min(min_ending+nums[i],nums[i])
        min_sum=min(min_ending,min_sum)

    if max_sum<0:
        return max_sum

    circular_sum=total_sum-min_sum

    return max(max_sum,circular_sum)

        

if __name__=="__main__":
    nums=[5,-1,-2,-7,3]
    print(circular_subarray_sum(nums))

