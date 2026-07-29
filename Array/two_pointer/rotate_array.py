def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

def rotate(nums,k):
    k=k%len(nums)
    reverse(nums,0,len(nums)-1)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)
    return nums


if __name__=="__main__":
    nums=[1,2,3,4,5,6,7]
    k=3
    print(rotate(nums,k))