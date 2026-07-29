def two_sum(nums:list[int], target):
    nums=sorted(nums)
    n=len(nums)

    i=0
    j=n-1

    while (i<j):
        sum=nums[i]+nums[j]

        if sum==target:
            return (nums[i],nums[j])
        elif sum>target:
            j=j-1
        else:
            i=i+1
    return ("Empty")

if __name__=="__main__":
    nums=[2,3,4,5]
    target=6
    print(two_sum(nums,target))