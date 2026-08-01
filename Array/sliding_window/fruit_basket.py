"""
Algorithm:
low=0
high=0
freq={}
res=-1

for high (0->len(nums)):
  freq[nums[high]]=freq.get(nums[high],0)+1
  while len(freq)>2:
    freq[nums[low]]-=1

    if freq[nums[low]]==0:
       del freq[nums[low]] from freq
    low++
  if len(freq)<=2:
    length=high-low+1
    if length>res:
      res=length
return the res
      
   

"""

# CODE:

def fruit_basket(nums,k):
    low=0
    high=0
    freq={}
    res=-1

    for high in range(len(nums)):
        freq[nums[high]]=freq.get(nums[high],0)+1
        while (len(freq)>2):
            freq[nums[low]]-=1
            if freq[nums[low]]==0:
                del freq[nums[low]]
            low+=1
        if len(freq)<=2:
            length=high-low+1 
            if length>res:
                res=length 
    return res 

if __name__=="__main__":
    nums=[1,1,2,2,3,4]
    k=2 
    print(fruit_basket(nums,k))

    """

    DRY RUN:

    Input:
nums = [1,1,2,2,3,4]

---------------------------------------------------------------------------------------------------------------
| Step | high | nums[high] | low | Action                      | HashMap            | Window        | Length | res |
---------------------------------------------------------------------------------------------------------------
| 0    |  -   |     -      |  0  | Initialize                  | {}                 | []            |   -    | -1  |
| 1    |  0   |     1      |  0  | Add 1                       | {1:1}              | [1]           |   1    |  1  |
| 2    |  1   |     1      |  0  | Add 1                       | {1:2}              | [1,1]         |   2    |  2  |
| 3    |  2   |     2      |  0  | Add 2                       | {1:2,2:1}          | [1,1,2]       |   3    |  3  |
| 4    |  3   |     2      |  0  | Add 2                       | {1:2,2:2}          | [1,1,2,2]     |   4    |  4  |
| 5    |  4   |     3      |  0  | Add 3                       | {1:2,2:2,3:1}      | [1,1,2,2,3]   |   -    |  4  |
| 6    |  4   |     3      |  1  | Remove 1                    | {1:1,2:2,3:1}      | [1,2,2,3]     |   -    |  4  |
| 7    |  4   |     3      |  2  | Remove 1, Delete key        | {2:2,3:1}          | [2,2,3]       |   3    |  4  |
| 8    |  5   |     4      |  2  | Add 4                       | {2:2,3:1,4:1}      | [2,2,3,4]     |   -    |  4  |
| 9    |  5   |     4      |  3  | Remove 2                    | {2:1,3:1,4:1}      | [2,3,4]       |   -    |  4  |
| 10   |  5   |     4      |  4  | Remove 2, Delete key        | {3:1,4:1}          | [3,4]         |   2    |  4  |
---------------------------------------------------------------------------------------------------------------

Final Answer:
res = 4

   
    
    """