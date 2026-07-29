def sqr_of_sorted_array(nums:list[int])->list[int]:
    i=0
    j=len(nums)-1
    k=len(nums)-1
    temp=[0]*len(nums)

    while i<=j:
        if abs(nums[i])>abs(nums[j]):
            temp[k]=nums[i]*nums[i]
            i+=1
        else:
            temp[k]=nums[j]*nums[j]
            j-=1
        k-=1
    return temp
        
if __name__=="__main__":
    nums=[-4,-1,0,3,10]
    print(sqr_of_sorted_array(nums))