"""
ALGORITHM:



low=0
high=0
n=len(nums)
maximum_sum=-float(inf)
current_sum=0
freq={}
for high in range(n):
   freq[nums[high]]=freq.get(nums[high],0)+1

   current_sum+=nums[high]

   while (freq[nums[high]])>1:
      freq[nums[low]]-=1
      current_sum-=nums[low]

      if frq[nums[low]]==0:
         del freq(nums[low])
      low+=1

    if current_sum>maximum_sum:
        maximum_sum=current_sum

return maximum_sum

"""



def maximum_erasure_value(nums):

     low=0 
     high=0
     current_sum=0
     maximum_sum=-float("Inf")
     freq={}

     for high in range(len(nums)):
          freq[nums[high]]=freq.get(nums[high],0)+1
          current_sum+=nums[high]

          while(freq[nums[high]])>1:
               freq[nums[low]]-=1
               current_sum-=nums[low]
               if freq[nums[low]]==0:
                    del freq[nums[low]]
               low+=1
          if current_sum>maximum_sum:
               maximum_sum=current_sum

     return maximum_sum


if __name__=="__main__":
     nums=[4,2,4,5,6]
     print(maximum_erasure_value(nums))


"""

DRY RUN:

Input:
nums = [4, 2, 4, 5, 6]

Initial Values:
----------------------------------------------------------
low = 0
current_sum = 0
maximum_sum = -∞
freq = {}
----------------------------------------------------------

+------+-----+-----------+-------------------------+-------------+------------------------------+-----+-------------+-------------+
|Step  |High | nums[high]| Frequency Map           | Current Sum | Action                       | Low | Valid Window| Maximum Sum |
+------+-----+-----------+-------------------------+-------------+------------------------------+-----+-------------+-------------+
| 1    | 0   |     4     | {4:1}                   |      4      | Unique, update answer        |  0  | [4]         |      4      |
| 2    | 1   |     2     | {4:1,2:1}               |      6      | Unique, update answer        |  0  | [4,2]       |      6      |
| 3    | 2   |     4     | {4:2,2:1}               |     10      | Duplicate found              |  0  | [4,2,4]     |      6      |
|      |     |           | {4:1,2:1}               |      6      | Remove nums[0]=4, low++      |  1  | [2,4]       |      6      |
| 4    | 3   |     5     | {2:1,4:1,5:1}           |     11      | Unique, update answer        |  1  | [2,4,5]     |     11      |
| 5    | 4   |     6     | {2:1,4:1,5:1,6:1}       |     17      | Unique, update answer        |  1  | [2,4,5,6]   |     17      |
+------+-----+-----------+-------------------------+-------------+------------------------------+-----+-------------+-------------+

Final Answer:
----------------------------------------------------------
maximum_sum = 17
----------------------------------------------------------

Output:
17


TIME COMPLEXITY:
O(n)

SPACE COMPLEXITY:
O(n)




"""