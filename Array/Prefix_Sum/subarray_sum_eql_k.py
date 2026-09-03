def Subarray_sum_equal_k(nums,k):
    prefix_sum=0
    count=0
    freq={0:1}

    for num in nums:
        prefix_sum+=num 
        required=prefix_sum-k 

        if required in freq:
            count+=freq[required]

        freq[prefix_sum]=freq.get(prefix_sum,0)+1 

    return count 


if __name__=="__main__":
    nums=[1,2,3]
    print(Subarray_sum_equal_k(nums,3))


"""

SUBARRAY SUM EQUALS K — PREFIX SUM + HASHMAP
Revision Notes

1. PROBLEM
Given an integer array nums and an integer k, find the number of continuous subarrays whose sum is exactly k.

Example:
nums = [1, 2, 3], k = 3

Valid subarrays:
[1, 2] -> 3
[3] -> 3

Answer = 2


2. CORE IDEA
Use:
    Prefix Sum + HashMap (Frequency Map)

Maintain:
    prefix_sum = sum of elements seen so far

Suppose:
    current_prefix_sum = S

For a previous prefix sum P:

    S - P = k

Therefore:

    P = S - k

So, at every element:
1. Add the current number to prefix_sum.
2. Calculate required = prefix_sum - k.
3. Check how many times required has appeared before.
4. Add that frequency to the answer.
5. Store the current prefix_sum in the HashMap.


3. WHY PREFIX SUM WORKS
If:

    prefix[i] = nums[0] + nums[1] + ... + nums[i]

Then the sum of a subarray from index j+1 to i is:

    prefix[i] - prefix[j]

If this difference equals k:

    prefix[i] - prefix[j] = k

Then:

    prefix[j] = prefix[i] - k

This is why we search for:
    current_prefix_sum - k


4. IMPORTANT INITIALIZATION
Always start with:

    freq = {0: 1}

Meaning:
    Prefix sum 0 has appeared once before the array starts.

Why is this necessary?

Example:
    nums = [1, 2]
    k = 3

After processing 1 and 2:

    prefix_sum = 3

We need:

    prefix_sum - k = 3 - 3 = 0

The 0 in the map allows us to count [1, 2], which starts at index 0.

Without {0: 1}, subarrays starting from index 0 could be missed.


5. WHY STORE FREQUENCY?
We don't just need to know whether a prefix sum exists.
The same prefix sum can appear multiple times.

Example:
    nums = [1, -1, 1, -1]
    k = 0

Prefix sums:
    0, 1, 0, 1, 0

A prefix sum such as 0 can occur several times.

If:
    freq[0] = 3

then there are 3 previous positions that can form valid subarrays with the current position.

Therefore the HashMap stores:

    prefix_sum -> frequency


6. COMPLETE ALGORITHM
Initialize:

    prefix_sum = 0
    count = 0
    freq = {0: 1}

For every num in nums:

    prefix_sum += num

    required = prefix_sum - k

    if required exists in freq:
        count += freq[required]

    freq[prefix_sum] += 1

Return count.


7. PYTHON CODE

def subarraySum(nums, k):
    prefix_sum = 0
    count = 0

    freq = {0: 1}

    for num in nums:
        prefix_sum += num

        required = prefix_sum - k

        if required in freq:
            count += freq[required]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


8. STEP-BY-STEP DRY RUN

Input:
    nums = [1, 2, 3]
    k = 3

Initial:
    prefix_sum = 0
    count = 0
    freq = {0: 1}

Step 1:
    num = 1
    prefix_sum = 1
    required = 1 - 3 = -2
    -2 not found

    count = 0
    freq = {0:1, 1:1}

Step 2:
    num = 2
    prefix_sum = 3
    required = 3 - 3 = 0
    0 found once

    count = 0 + 1 = 1
    freq = {0:1, 1:1, 3:1}

Valid subarray:
    [1, 2]

Step 3:
    num = 3
    prefix_sum = 6
    required = 6 - 3 = 3
    3 found once

    count = 1 + 1 = 2
    freq = {0:1, 1:1, 3:1, 6:1}

Valid subarray:
    [3]

Final answer:
    2


9. EASY WAY TO REMEMBER

Think:

    CURRENT SUM - OLD SUM = K

Therefore:

    OLD SUM = CURRENT SUM - K

So:

    Look for (prefix_sum - k) in HashMap.


10. COMMON MISTAKES

Mistake 1:
Forgetting:
    freq = {0: 1}

Mistake 2:
Using a Set instead of a Frequency Map.

Wrong:
    set of prefix sums

Correct:
    prefix_sum -> frequency

Mistake 3:
Checking the HashMap after inserting the current prefix sum.

Correct order:
    1. Update prefix_sum
    2. Search for prefix_sum - k
    3. Add frequency to count
    4. Insert/update current prefix_sum

Mistake 4:
Using a sliding window when negative numbers are allowed.

For this general problem, Prefix Sum + HashMap works with positive, zero, and negative numbers.


11. COMPLEXITY

Time Complexity:
    O(n)

Space Complexity:
    O(n)

Reason:
    We traverse the array once and store prefix sums in a HashMap.


12. INTERVIEW INTUITION

If the current prefix sum is S and I want a subarray of sum K, I need an earlier prefix sum:

    S - K

If that earlier prefix sum appeared F times, then there are F valid subarrays ending at the current index.

So:

    count += freq[prefix_sum - k]


13. QUICK REVISION TEMPLATE

Problem:
    Count continuous subarrays with sum K.

Technique:
    Prefix Sum + HashMap

Formula:
    current_prefix - previous_prefix = K

Rearrange:
    previous_prefix = current_prefix - K

HashMap:
    prefix_sum -> frequency

Initialization:
    freq = {0: 1}

At each element:
    prefix_sum += num
    count += freq.get(prefix_sum - k, 0)
    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

Complexity:
    O(n) time
    O(n) space


14. ONE-LINE MEMORY TRICK

    "Current Prefix - K = Prefix I Need"

This single line is the key to remembering the entire solution.



"""