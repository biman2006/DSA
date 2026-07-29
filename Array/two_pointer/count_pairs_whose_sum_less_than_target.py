def count_pairs_whose_sum_is_less_than_target(nums,target):
    i=0
    j=len(nums)-1
    count=0
    nums.sort()

    while i<j:
        if nums[i]+nums[j]<target:
            count+=(j-1)
            i+=1
        else:
            j-=1
    return count

if __name__=="__main__":
    nums=[1,1,2,1]
    target=3
    print(count_pairs_whose_sum_is_less_than_target(nums,target))