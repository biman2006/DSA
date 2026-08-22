def Bubble_sort(nums:list[int])->list[int]:
    swap_count=0
    for i in range(0,len(nums)):

        print(f"\n---- Pass {i+1}---")
        flag=0
        for j in range(0,len(nums)-1-i):
            print(f"Compare {nums[j]} and {nums[j+1]}")
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swap_count+=1
                flag=1
                print(f"swap -> {nums}")
        
            print(f"After Pass {i+1}:{nums}")
        if flag==0:
            break 
    print(f"Total swaps: {swap_count}")
    return nums




if __name__=="__main__":
    nums=[15,16,6,8,5]

    res=Bubble_sort(nums)
    print(res)





# NOTES

''' 
1. Algorithm
Start from index 0.
Compare arr[j] and arr[j+1].
Swap if arr[j] > arr[j+1].
Continue until the last unsorted element.
Repeat for n-1 passes or stop early if no swaps occur.
'''

'''
2.Time Complexity
Case	                        Complexity
Best (already sorted, optimized)	O(n)
Average	                            O(n²)
Worst (reverse sorted)	            O(n²)

'''

'''
 3.Space Complexity
O(1)
No extra array is used.
It is an in-place sorting algorithm.

'''

'''
4.Stability

✅ Stable

Equal elements keep their original relative order.

Example:

Before:
5A 3 5B 2

After sorting:
2 3 5A 5B

5A stays before 5B.

'''

'''

5.In-place or Not?

✅ Yes

It sorts within the original array.

'''

'''
6.Adaptive or Not?
Normal Bubble Sort: ❌ No
Optimized Bubble Sort (using flag/swapped): ✅ Yes

The optimized version stops if the array is already sorted.

'''

'''
7.Number of Passes

For an array of size n:

Maximum passes = n − 1
Your outer loop may iterate n times, but the last iteration performs 0 comparisons because the inner loop range becomes empty.

'''

'''
8.Number of Comparisons
Worst Case

n(n−1)/2
	​


Example:

n = 5

4 + 3 + 2 + 1 = 10 comparisons

'''

'''

9.Number of Swaps
Best Case: 0
Worst Case: 

n(n−1)/2
	​


Bubble Sort performs one swap for each inversion in the array.

Example:

[4,3,2,1]

Swaps = 6



'''

