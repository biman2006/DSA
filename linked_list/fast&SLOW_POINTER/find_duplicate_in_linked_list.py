def duplicate_number(nums):
    slow=0
    fast=0
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]


        if slow==fast:
            break 
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow 
        



if __name__=="__main__":
    nums=[1,2,2,3,56]
    print(duplicate_number(nums))