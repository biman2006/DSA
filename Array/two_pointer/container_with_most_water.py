def container_with_most_water(nums):
    n=len(nums)
    left=0
    right=n-1
    max_area=0
    
    while left<right:
        if nums[left]<nums[right]:
            height=nums[left]
        else:
           height= nums[right]
        width=right-left 
        area=height*width
        max_area=max(area,max_area)
        if nums[left]<nums[right]:
            left+=1
        else:
            right-=1
    return max_area