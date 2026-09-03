def continuous_Subarray_sum(nums,k):
    remainder_map={0:-1}
    prefix_sum=0
    for i,num in enumerate(nums):
        prefix_sum+=num
        remainder=prefix_sum%k 

        if remainder in remainder_map:
            if i-remainder_map[remainder]>=2:
                return True 
        else:
            remainder_map[remainder]=i 
    return False 

if __name__=="__main__":
    nums=[23,2,4,6,7]
    print(continuous_Subarray_sum(nums,6))



""" 

CONTINUOUS SUBARRAY SUM — LEETCODE 523
PREFIX SUM + REMAINDER + HASHMAP
REVISION NOTES

1. PROBLEM
Given nums and k, return True if there is a continuous subarray
of at least 2 elements whose sum is a multiple of k.

That means:
    subarray_sum % k == 0

Example:
    nums = [23, 2, 4, 6, 7]
    k = 6

[2, 4] = 6, and 6 % 6 == 0
Answer = True


2. HOW TO RECOGNIZE THE PATTERN

"continuous subarray"  -> Prefix Sum
"divisible/multiple of k" -> Modulo (%)

Therefore:
    Prefix Sum + Remainder + HashMap


3. CORE MATHEMATICAL IDEA

For two prefix sums:

    prefix2 - prefix1 = subarray_sum

We need:

    (prefix2 - prefix1) % k == 0

This happens when:

    prefix2 % k == prefix1 % k

Therefore:

    SAME REMAINDER
        ->
    Difference is divisible by k
        ->
    Subarray sum is a multiple of k


Example:
    23 % 6 = 5
    29 % 6 = 5

Same remainder, so:
    29 - 23 = 6
and:
    6 % 6 = 0

The subarray is [2, 4].


4. WHAT THE HASHMAP STORES

Store:

    remainder -> first index

Example:
    {0: -1, 5: 0, 1: 1}

This means:
    remainder 0 first appeared at index -1
    remainder 5 first appeared at index 0
    remainder 1 first appeared at index 1


5. WHY {0: -1}?

Initialize:

    remainder_map = {0: -1}

Index -1 means "before the array starts".

This lets us detect valid subarrays starting at index 0.

Example:
    nums = [6, 1, 5]
    k = 6

At index 2:
    prefix_sum = 12
    12 % 6 = 0

We already have:
    0 -> -1

Length:
    2 - (-1) = 3

So [6, 1, 5] is valid.


6. WHY CHECK LENGTH >= 2?

The problem requires at least 2 elements.

Check:

    i - old_index >= 2

Example:
    nums = [6]
    k = 6

Remainder = 0
Old index = -1
Current index = 0

Length:
    0 - (-1) = 1

Only one element, so return False.


7. COMPLETE PYTHON CODE

def checkSubarraySum(nums, k):
    remainder_map = {0: -1}
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        remainder = prefix_sum % k

        if remainder in remainder_map:
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i

    return False


8. LINE-BY-LINE IDEA

remainder_map = {0: -1}
    Store remainder 0 before the array starts.

prefix_sum = 0
    Running sum.

for i, num in enumerate(nums):
    Visit every element and get its index.

prefix_sum += num
    Update running sum.

remainder = prefix_sum % k
    Get the current remainder.

if remainder in remainder_map:
    Same remainder appeared before.

if i - remainder_map[remainder] >= 2:
    Make sure at least 2 elements are in the subarray.

return True
    A valid subarray was found.

else:
    remainder_map[remainder] = i
    First time seeing this remainder, so remember its index.

return False
    No valid subarray exists.


9. COMPLETE DRY RUN

Input:
    nums = [23, 2, 4, 6, 7]
    k = 6

Initial:
    prefix_sum = 0
    remainder_map = {0: -1}


ITERATION 1
    i = 0
    num = 23

    prefix_sum = 23
    remainder = 23 % 6 = 5

    5 is NOT in the map.

    Store:
        5 -> 0

    Map:
        {0: -1, 5: 0}


ITERATION 2
    i = 1
    num = 2

    prefix_sum = 25
    remainder = 25 % 6 = 1

    1 is NOT in the map.

    Store:
        1 -> 1

    Map:
        {0: -1, 5: 0, 1: 1}


ITERATION 3
    i = 2
    num = 4

    prefix_sum = 29
    remainder = 29 % 6 = 5

    5 IS already in the map.

    It was first seen at index 0.

    Check:
        i - old_index
        = 2 - 0
        = 2

    2 >= 2 -> TRUE

    Therefore:
        return True


10. WHICH SUBARRAY DID WE FIND?

Prefix sum at index 0:
    23

Prefix sum at index 2:
    29

Difference:
    29 - 23 = 6

The elements between them are:
    [2, 4]

Sum:
    2 + 4 = 6

And:
    6 % 6 = 0

Therefore [2, 4] is a valid answer.


11. DRY RUN TABLE

    i    num    prefix_sum    remainder    action
    ------------------------------------------------
    0    23       23             5         store 5 -> 0
    1     2       25             1         store 1 -> 1
    2     4       29             5         found, length 2 -> TRUE

We stop at index 2 because the answer is already True.


12. WHY STORE ONLY THE FIRST INDEX?

If the same remainder appears multiple times, keep the earliest index.

Why?

The earliest index creates the longest possible subarray.

Example:
    remainder 5 first seen at index 0

If we later see 5 at index 2, keep:
    5 -> 0

Do not replace it with:
    5 -> 2


13. DIFFERENCE FROM SUBARRAY SUM EQUALS K

SUBARRAY SUM EQUALS K:

Condition:
    subarray_sum = K

Derivation:
    current_prefix - old_prefix = K

Therefore:
    old_prefix = current_prefix - K

So search for:
    current_prefix - K


CONTINUOUS SUBARRAY SUM:

Condition:
    subarray_sum % K = 0

Derivation:
    (current_prefix - old_prefix) % K = 0

Therefore:
    current_prefix % K == old_prefix % K

So search for:
    SAME REMAINDER


14. COMMON MISTAKES

1. Forgetting:
       {0: -1}

2. Using actual prefix sums instead of:
       prefix_sum % k

3. Forgetting:
       length >= 2

4. Replacing the first occurrence of a remainder.

5. Thinking same remainder means same prefix sum.
   They are different values; only their remainders are equal.


15. COMPLEXITY

Time:
    O(n)

Space:
    O(n)


16. INTERVIEW THINKING PROCESS

Step 1:
    Is it a continuous subarray?
    -> Think Prefix Sum.

Step 2:
    Is the sum divisible by K?
    -> Think % K.

Step 3:
    What makes a difference divisible by K?
    -> Same remainder.

Step 4:
    How do I remember previous remainders?
    -> HashMap.

Step 5:
    What does the map store?
    -> remainder -> first index.

Step 6:
    What extra condition exists?
    -> At least 2 elements.


17. ULTRA-SHORT REVISION

Problem:
    Continuous subarray of at least 2 elements
    whose sum is a multiple of K.

Technique:
    Prefix Sum + HashMap

Key formula:
    subarray_sum = prefix2 - prefix1

Need:
    (prefix2 - prefix1) % K == 0

Therefore:
    prefix2 % K == prefix1 % K

So:
    SAME REMAINDER = VALID SUBARRAY

Map:
    remainder -> first index

Initialize:
    {0: -1}

Length:
    current_index - old_index >= 2

Complexity:
    O(n) time
    O(n) space


18. ONE-LINE MEMORY TRICK

    "CONTINUOUS + DIVISIBLE
     -> PREFIX SUM % K
     -> FIND SAME REMAINDER"

END OF NOTES





"""
