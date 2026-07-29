def selection_sort(nums:list[int])->list[int]:
    swap_count=0
    comparison_count=0
    for i in range(len(nums)):
        min_elem=i

        for j in range(i+1,len(nums)):
            comparison_count+=1
            if nums[j]<nums[min_elem]:
                min_elem=j
        if min_elem!=i:
         nums[i],nums[min_elem]=nums[min_elem],nums[i]
         swap_count+=1
        print(f"Pass {i+1}:{nums}")

    print("Swaps:", swap_count)
    print("Comparison:", comparison_count)
    return nums 

if __name__=="__main__":
    nums=[2,4,1,7]

    res=selection_sort(nums)
    print(res)