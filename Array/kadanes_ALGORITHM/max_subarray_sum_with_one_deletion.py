def max_sub_array_sum_with_one_deletion(nums):
    nodel=nums[0]
    onedel=float("-inf")
    res=nums[0]

    for i in range(1,len(nums)):
        old_nodel=nodel
        nodel=max(nodel+nums[i],nums[i])
        onedel=max(onedel+nums[i],old_nodel)
        res=max(res,nodel,onedel)

    return res 


if __name__=="__main__":
    nums=[1,-2,3,4]
    print(max_sub_array_sum_with_one_deletion(nums))


"""

Maximum Subarray Sum With One Deletion — Simple Explanation

Idea

This is a modified Kadane's Algorithm.

We maintain 2 values:

1. no_delete → maximum sum ending at current index without deleting anything.
2. one_delete → maximum sum ending at current index after deleting one element.

Algorithm

For every element arr[i]:

Step 1 — Don't delete anything:
no_delete = max(no_delete + arr[i], arr[i])

Step 2 — Delete one element:
one_delete = max(one_delete + arr[i], old_no_delete)

Here:
- one_delete + arr[i] → we already deleted an element earlier.
- old_no_delete → delete the current element.

Step 3 — Update answer:
ans = max(ans, no_delete, one_delete)

Example

arr = [1, -2, 0, 3]

Delete -2:

[1, 0, 3]

Sum:
1 + 0 + 3 = 4

So the answer is 4.

Complexity

- Time: O(n) — visit each element once.
- Space: O(1) — only a few variables are used.

Remember

Normal Kadane = 1 state
Kadane + one deletion = 2 states (no_delete, one_delete)



"""