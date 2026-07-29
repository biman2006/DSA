def sorted_rotated(nums:list[int])->list[int]:
    count =0
    for i in range(len(nums)):
        if nums[i]>nums[(i+1)%len(nums)]:
            count+=1
    if count<=1:
        return True
    else:
        return False 
if __name__=="__main__":
    nums=[1,2,3,4,2]
    print(sorted_rotated(nums))
