"""

MAXIMUM SUBARRAY SUM — KADANE'S ALGORITHM

Goal:
Find the contiguous subarray with the maximum possible sum.

Idea:
For every element nums[i], decide:
1. Extend the previous subarray: best_ending + nums[i]
2. Start a new subarray from nums[i]

best_ending = maximum sum of a subarray ending at the current index.
ans = maximum sum found so far.

Algorithm:
1. Initialize:
   best_ending = nums[0]
   ans = nums[0]
2. Loop i from 1 to len(nums)-1.
3. Calculate:
   v1 = best_ending + nums[i]
   v2 = nums[i]
4. Set best_ending = max(v1, v2).
5. Set ans = max(ans, best_ending).
6. Return ans.

Time Complexity: O(n)
Space Complexity: O(1)

For nums = [-2, 1, -3, 4, -1, 2]
Maximum subarray = [4, -1, 2]
Maximum sum = 5



"""


def max_sum_subarray(nums):
    best_ending=nums[0]
    ans=nums[0]

    for i in range(1,len(nums)):
        v1=best_ending+nums[i]
        v2=nums[i]

        if v1>v2:
            best_ending=v1 
        else:
            best_ending=v2 

        if ans>best_ending:
            ans=ans
        else:
            ans=best_ending 
    return ans 



if __name__=="__main__":
    nums=[-2,1,-3,4,-1,2]
    print(max_sum_subarray(nums))



"""

MAXIMUM SUBARRAY — DRY RUN

Input:
nums = [-2, 1, -3, 4, -1, 2]

Initial:
best_ending = -2
ans = -2

i=1, nums[i]=1
v1 = -2 + 1 = -1
v2 = 1
best_ending = max(-1, 1) = 1
ans = max(-2, 1) = 1

i=2, nums[i]=-3
v1 = 1 + (-3) = -2
v2 = -3
best_ending = max(-2, -3) = -2
ans = max(1, -2) = 1

i=3, nums[i]=4
v1 = -2 + 4 = 2
v2 = 4
best_ending = max(2, 4) = 4
ans = max(1, 4) = 4

i=4, nums[i]=-1
v1 = 4 + (-1) = 3
v2 = -1
best_ending = max(3, -1) = 3
ans = max(4, 3) = 4

i=5, nums[i]=2
v1 = 3 + 2 = 5
v2 = 2
best_ending = max(5, 2) = 5
ans = max(4, 5) = 5

Final:
ans = 5

Maximum subarray:
[4, -1, 2]

Output:
5

Compact table:
i   value   v1   v2   best_ending   ans
0   -2      -    -       -2         -2
1    1     -1    1        1          1
2   -3     -2   -3       -2          1
3    4      2    4        4          4
4   -1      3   -1        3          4
5    2      5    2        5          5




"""
