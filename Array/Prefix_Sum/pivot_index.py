def pivotIndex(nums):
    left=0
    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
    for i in range(len(nums)):
        right=sum-nums[i]-left

        if left==right:
            return i
        left+=nums[i]

    return -1

if __name__=="__main__":
    nums=[1,7,3,6,5,6]

    print(pivotIndex(nums))