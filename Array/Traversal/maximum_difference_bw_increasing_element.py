def max_diff_bw_increasing_elem(nums:list[int])->list[int]:
    min_val=nums[0]
    max_diff=-1

    for j in range(1,len(nums)-1):
        if nums[j]>min_val:
            diff=nums[j]-min_val
            max_diff=diff 
        if nums[j]<min_val:
            min_val=nums[j]

    return max_diff

if __name__=="__main__":
    nums=[7,1,5,4]
    res=max_diff_bw_increasing_elem(nums)
    print(res)

