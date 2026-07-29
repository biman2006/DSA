def triplet_smaller(nums,target):
    nums.sort()
    n=len(nums)
    i=0
    
    ans=0

    for i in range(n-1):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=n-1

        while left<right:
            sum=nums[i]+nums[left]+nums[right]

            if sum>=target:
                right-=1
            else:
                ans+=(right-left)
                left+=1
    return ans


if __name__=="__main__":
    nums=[-2,0,1,3]
    target=3
    print(triplet_smaller(nums,target))

