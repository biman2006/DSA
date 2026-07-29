def largest_element_in_array(nums:list[int])->list[int]:
    largest_element=nums[0]
    for i in range(len(nums)):
        

        if nums[i]>largest_element:
            largest_element=nums[i]
    return largest_element


if __name__=="__main__":
    nums=[12,43,32,6]
    res=largest_element_in_array(nums)
    print(res)