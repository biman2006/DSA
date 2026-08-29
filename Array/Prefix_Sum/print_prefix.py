def print_prefix_sum(nums):
    result_prefix_sum=[]
    sum=0

    for i in range(len(nums)):
        
        result_prefix_sum.append(sum)
        sum+=nums[i]
        
    return result_prefix_sum

if __name__=="__main__":
    nums=[4,6,3,2,1]
    print(print_prefix_sum(nums))
