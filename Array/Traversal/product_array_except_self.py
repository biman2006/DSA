

def product_array_except_self2(nums:list[int])->list[int]:
    
    suffix=1
    result=[1]*len(nums)

    for i in range(1,len(nums)):
        result[i]=nums[i-1]*result[i-1]

    for i in range(len(nums)-2,-1,-1):
        suffix*=nums[i+1]
        result[i]*=suffix

    
    return result

if __name__=="__main__":
    nums=[1,2,3,4]
    res=product_array_except_self2(nums)
    print(res) 





