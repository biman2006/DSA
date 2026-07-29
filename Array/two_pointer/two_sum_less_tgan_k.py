def two_sum_less_than_k(nums,k):
    i=0
    j=len(nums)-1
    nums=sorted(nums)
    max_sum=-1
    

    while i<j:
        if nums[i]+nums[j]>=k:
            j-=1
        if nums[i]+nums[j]<=k:
            max_sum=max(max_sum,nums[i]+nums[j])
            i+=1
    return max_sum

if __name__=="__main__":
    nums=[34,23,1,24,75,33,54,8]
    k=60
    print(two_sum_less_than_k(nums,k))