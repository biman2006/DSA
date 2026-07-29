def remove_duplicate(nums:list[int])->list[int]:
    i=0
    j=1
    no_of_unique=1

    while(j<len(nums)):
        if (nums[j]==nums[j-1]):
            j+=1
            continue
        else:
            nums[i+1]=nums[j]
            i+=1
            no_of_unique+=1
            j+=1
    return (no_of_unique,nums)

            


    
if __name__=="__main__":
    nums=[1,1,1,2,2,3]
    print(remove_duplicate(nums))
