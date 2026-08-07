def atMost(nums,k):
    low=0
    n=len(nums)
    odd_count=0
    answer=0
    for high in range(n):
        if nums[high]%2==1:
            odd_count+=1

        while odd_count>k:
            if nums[low]%2==1:
                odd_count-=1
            low+=1

        answer+=high-low+1 
    return answer 
def numberofSubarray(nums,k):
    return atMost(nums,k)-atMost(nums,k-1)

if __name__=="__main__":
    nums=[2,1,2,1]
    k=2
    print(numberofSubarray(nums,k))



"""

===========================================================
DRY RUN : atMost(nums, 1)
===========================================================

Input:
nums = [2, 1, 2, 1]
k = 1

Initial State:
low = 0
odd_count = 0
answer = 0

+------+-----+-----------+------+-----------+-------------------------+-----+----------------+------------+--------+
|Step  |high |nums[high] | Odd? | odd_count | Action                  | low | Window         | Add Value  | answer |
+------+-----+-----------+------+-----------+-------------------------+-----+----------------+------------+--------+
|Start |  -  |     -     |  -   |     0     | Initialize              |  0  | []             |     -      |   0    |
|  1   |  0  |     2     |  No  |     0     | Valid                   |  0  | [2]            |     1      |   1    |
|  2   |  1  |     1     | Yes  |     1     | Valid                   |  0  | [2,1]          |     2      |   3    |
|  3   |  2  |     2     |  No  |     1     | Valid                   |  0  | [2,1,2]        |     3      |   6    |
|  4   |  3  |     1     | Yes  |     2     | Invalid -> Shrink       |  2  | [2,1]          |     2      |   8    |
+------+-----+-----------+------+-----------+-------------------------+-----+----------------+------------+--------+

-----------------------------------------------------------
Shrinking Process (Step 4)
-----------------------------------------------------------

Current Window = [2,1,2,1]
odd_count = 2

Remove nums[0] = 2 (Even)
low = 1
odd_count = 2

Remove nums[1] = 1 (Odd)
low = 2
odd_count = 1

Window becomes:
[2,1]

Add:
answer += high - low + 1
answer += 3 - 2 + 1
answer += 2

Final:
atMost(nums,1) = 8


===========================================================
DRY RUN : atMost(nums, 0)
===========================================================

Input:
nums = [2,1,2,1]
k = 0

Initial State:
low = 0
odd_count = 0
answer = 0

+------+-----+-----------+------+-----------+-------------------------+-----+----------------+------------+--------+
|Step  |high |nums[high] | Odd? | odd_count | Action                  | low | Window         | Add Value  | answer |
+------+-----+-----------+------+-----------+-------------------------+-----+----------------+------------+--------+
|Start |  -  |     -     |  -   |     0     | Initialize              |  0  | []             |     -      |   0    |
|  1   |  0  |     2     |  No  |     0     | Valid                   |  0  | [2]            |     1      |   1    |
|  2   |  1  |     1     | Yes  |     1     | Invalid -> Shrink       |  2  | []             |     0      |   1    |
|  3   |  2  |     2     |  No  |     0     | Valid                   |  2  | [2]            |     1      |   2    |
|  4   |  3  |     1     | Yes  |     1     | Invalid -> Shrink       |  4  | []             |     0      |   2    |
+------+-----+-----------+------+-----------+-------------------------+-----+----------------+------------+--------+

-----------------------------------------------------------
Shrinking Process (Step 2)
-----------------------------------------------------------

Current Window = [2,1]
odd_count = 1

Remove nums[0] = 2 (Even)
low = 1
odd_count = 1

Remove nums[1] = 1 (Odd)
low = 2
odd_count = 0

Window becomes:
[]

Add:
answer += high - low + 1
answer += 1 - 2 + 1
answer += 0

-----------------------------------------------------------
Shrinking Process (Step 4)
-----------------------------------------------------------

Current Window = [2,1]
odd_count = 1

Remove nums[2] = 2 (Even)
low = 3
odd_count = 1

Remove nums[3] = 1 (Odd)
low = 4
odd_count = 0

Window becomes:
[]

Add:
answer += high - low + 1
answer += 3 - 4 + 1
answer += 0

Final:
atMost(nums,0) = 2


===========================================================
FINAL ANSWER
===========================================================

Exactly K Odd Numbers

= atMost(1) - atMost(0)

= 8 - 2

= 6


===========================================================
TIME COMPLEXITY
===========================================================

high pointer moves from left to right once.

high:
0 -> 1 -> 2 -> 3

low pointer also moves from left to right once.

low:
0 -> 1 -> 2 -> 3 -> 4

Each pointer visits every index at most one time.

Time Complexity  : O(n)

Space Complexity : O(1)



"""

