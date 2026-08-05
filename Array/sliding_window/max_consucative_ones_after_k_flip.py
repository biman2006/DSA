"""

ALGORITHM:

low=0
high=0
count=0
max_len=0

for high->len(nums):
   if nums[high]=0:
      count+=1
    when count>K:
    repeat this process(
      shrink the window until count<k)


return max_len



"""


def max_consucative_ones_after_k_flip(nums,k):

    low=0
    high=0
    count=0
    maximum_length=0

    for high in range(len(nums)):
        if nums[high]==0:
            count+=1
        while count>k:
            if nums[low]==0:
                count-=1

            low+=1
        length=high-low+1

        if length>maximum_length:
          maximum_length=length

    return maximum_length



if __name__=="__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2

    print(max_consucative_ones_after_k_flip(nums,k))



    """


    DRY RUN:


    Input:
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

Initial:
left = 0
zeroCount = 0
maxLength = 0

+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+
|Step  | right | nums[right] | zeroCount | left | Window (left...right)         | WindowSize | maxLength |
+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+
| 1    |   0   |      1      |     0     |  0   | [1]                           |     1      |     1     |
| 2    |   1   |      1      |     0     |  0   | [1,1]                         |     2      |     2     |
| 3    |   2   |      1      |     0     |  0   | [1,1,1]                       |     3      |     3     |
| 4    |   3   |      0      |     1     |  0   | [1,1,1,0]                     |     4      |     4     |
| 5    |   4   |      0      |     2     |  0   | [1,1,1,0,0]                   |     5      |     5     |
+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+

Step 6:
right = 5
nums[right] = 0

zeroCount = 3 (> k)

Shrink the window:

left = 0 -> nums[0] = 1
zeroCount = 3
left = 1

left = 1 -> nums[1] = 1
zeroCount = 3
left = 2

left = 2 -> nums[2] = 1
zeroCount = 3
left = 3

left = 3 -> nums[3] = 0
zeroCount = 2
left = 4

Now:
Window = [0,0]
Window Size = 5 - 4 + 1 = 2

maxLength = 5

+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+
|Step  | right | nums[right] | zeroCount | left | Window (left...right)         | WindowSize | maxLength |
+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+
| 6    |   5   |      0      |     2     |  4   | [0,0]                         |     2      |     5     |
| 7    |   6   |      1      |     2     |  4   | [0,0,1]                       |     3      |     5     |
| 8    |   7   |      1      |     2     |  4   | [0,0,1,1]                     |     4      |     5     |
| 9    |   8   |      1      |     2     |  4   | [0,0,1,1,1]                   |     5      |     5     |
|10    |   9   |      1      |     2     |  4   | [0,0,1,1,1,1]                 |     6      |     6     |
+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+

Step 11:
right = 10
nums[right] = 0

zeroCount = 3 (> k)

Shrink:

left = 4 -> nums[4] = 0
zeroCount = 2
left = 5

Now:
Window = [0,1,1,1,1,0]
Window Size = 10 - 5 + 1 = 6

maxLength = max(6,6) = 6

+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+
|Step  | right | nums[right] | zeroCount | left | Window (left...right)         | WindowSize | maxLength |
+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+
|11    |  10   |      0      |     2     |  5   | [0,1,1,1,1,0]                 |     6      |     6     |
+------+-------+-------------+-----------+------+-------------------------------+------------+-----------+

Final Answer:
maxLength = 6




TIME COMPLEXITY:
O(n)


SPACE COMPLEXITY:
O(1)
    
    
    
    
    
    
    
    
    
    
    """

