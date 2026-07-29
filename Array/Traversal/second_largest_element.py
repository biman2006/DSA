def second_largest_element(nums:list[int])->list[int]:
    largest=float("-inf")
    second_largest=float("-inf")
    n=len(nums)

    for i in range(0,n):
        if nums[i]>largest:
            second_largest=largest
            largest=nums[i]
        elif nums[i]>second_largest and nums[i]!=largest:
            second_largest=nums[i]

    return second_largest


if __name__=="__main__":
    nums=[4,2,6,8]
    res=second_largest_element(nums)
    print(res)
