def move_zeroes(nums:list[int])->list[int]:
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j],nums[i]=nums[i],nums[j]
            j+=1
    return nums 


if __name__=="__main__":
    nums=[1,0,3,0,4,0]
    print(move_zeroes(nums))
