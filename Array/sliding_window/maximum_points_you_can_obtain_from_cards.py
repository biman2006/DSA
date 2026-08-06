"""

ALGORITHM:
n=len(nums)

total_sum=total sum of the array

window size=n-k

if window_size==0:
  return total_sum

low=0
high=0
current_sum=0
minimum_length=float(inifinity)

for high in range len(nums):
   current_sum+=nums[high]

   while (high-low+1>windo_size):
      current_sum-=nums[low]
      low++

    if (high-low+1)==window_size:
       minimum_window_sum=min(minimum_window_sum,current_sum)

ans=total_sum-minimum_window_sum

return ans 

"""


def maximum_point_you_can_obtain_from_cards(nums,k):

    total_sum=0
    window_size=len(nums)-k

    for i in range(len(nums)):
        total_sum+=nums[i]

    if window_size==0:
        return total_sum
    low=0
    high=0
    current_sum=0
    minimum_window_sum=float('Inf')

    for high in range(len(nums)):
        current_sum+=nums[high]

        while high-low+1>window_size:
            current_sum-=nums[low]
            low+=1
        if high-low+1==window_size:
            minimum_window_sum=min(minimum_window_sum,current_sum)

    ans=total_sum-minimum_window_sum
    return ans 


if __name__=="__main__":

    nums=[1,2,3,4,5,6,1]
    k=3
    print(maximum_point_you_can_obtain_from_cards(nums,k))


"""

DRY RUN:

Input:
nums = [1, 2, 3, 4, 5, 6, 1]
k = 3

n = 7
window_size = n - k = 4
total_sum = 22

Initial Values:
-------------------------------------------------------------
low = 0
current_sum = 0
minimum_window_sum = ∞
-------------------------------------------------------------

+------+-----+-----------+-------------+-------------+------------------------+-----+--------------------+--------------------+
|Step  |High | nums[high]| current_sum | Window Size | Action                 | Low | current_sum (Final)| minimum_window_sum |
+------+-----+-----------+-------------+-------------+------------------------+-----+--------------------+--------------------+
| 1    | 0   |     1     |      1      |      1      | Window < 4             |  0  |         1          |        ∞           |
| 2    | 1   |     2     |      3      |      2      | Window < 4             |  0  |         3          |        ∞           |
| 3    | 2   |     3     |      6      |      3      | Window < 4             |  0  |         6          |        ∞           |
| 4    | 3   |     4     |     10      |      4      | Update minimum         |  0  |        10          |       10           |
| 5    | 4   |     5     |     15      |      5      | Remove nums[0] = 1     |  1  |        14          |       10           |
| 6    | 5   |     6     |     20      |      5      | Remove nums[1] = 2     |  2  |        18          |       10           |
| 7    | 6   |     1     |     19      |      5      | Remove nums[2] = 3     |  3  |        16          |       10           |
+------+-----+-----------+-------------+-------------+------------------------+-----+--------------------+--------------------+

Windows Considered:
-------------------------------------------------
[1,2,3,4]  -> Sum = 10  -> Minimum = 10
[2,3,4,5]  -> Sum = 14  -> Minimum = 10
[3,4,5,6]  -> Sum = 18  -> Minimum = 10
[4,5,6,1]  -> Sum = 16  -> Minimum = 10
-------------------------------------------------

Final Calculation:
-------------------------------------------------
total_sum = 22
minimum_window_sum = 10

answer = total_sum - minimum_window_sum
       = 22 - 10
       = 12
-------------------------------------------------

Output:
12

TIME COMPLEXITY:

O(n)

SPACE COMPLEXITY:
O(1)





"""