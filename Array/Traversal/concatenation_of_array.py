def concatenation_of_array(nums:list[int])->list[int]:
    #list=[]

    for i in range(len(nums)):
        nums.append(nums[i])

    #for num in nums:
       # list.append(num)

    return nums

if __name__=="__main__":
    nums=[1,2,1]
    result=concatenation_of_array(nums)

    print(result)