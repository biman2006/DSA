def Bubble_sort(nums:list[int])->list[int]:
    swap_count=0
    for i in range(0,len(nums)):

        print(f"\n---- Pass {i+1}---")
        flag=0
        for j in range(0,len(nums)-1-i):
            print(f"Compare {nums[j]} and {nums[j+1]}")
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swap_count+=1
                flag=1
                print(f"swap -> {nums}")
        
            print(f"After Pass {i+1}:{nums}")
        if flag==0:
            break 
    print(f"Total swaps: {swap_count}")
    return nums




if __name__=="__main__":
    nums=[15,16,6,8,5]

    res=Bubble_sort(nums)
    print(res)
    