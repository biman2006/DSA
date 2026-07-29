def triplet_sum(nums,target):
    nums.sort()
    n=len(nums)
    res=[]

    for i in range(n-1):

        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=n-1

        while left<right:
            current_sum=nums[i]+nums[left]+nums[right]

            if current_sum==target:
                res.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1

                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1

            elif current_sum<target:
                left+=1
            else:
                right-=1  
    return res  
   

if __name__=="__main__":
    nums=[2,3,6,4,9,4,4,4,4,2,7,9,55,3,26,14,10,5,33,10,12,44,20,30,6]
    target=100
    print(triplet_sum(nums,target))                