def max_vowel_in_a_substring(s,k):
    low=0
    high=k-1
    count=0
    vowels={'a','e','i','o','u'}

    for i in range(high):
        if s[i] in vowels:
            count+=1
    max_vowel=count 

    while high<len(s):
        if s[low] in vowels:
            count-=1
        low+=1
        high+=1

        if s[high] in vowels:
            count+=1

        max_vowel=max(count,max_vowel)

    return max_vowel


"""

DRY RUN:

Input:
s = "abciiidef"
k = 3

Index : 0 1 2 3 4 5 6 7 8
Char  : a b c i i i d e f

==========================================================
STEP 1 : BUILD FIRST WINDOW
==========================================================

low = 0
high = k - 1 = 2
count = 0

Window = [a b c]

i = 0
Character = a
Vowel? YES
count = 1

i = 1
Character = b
Vowel? NO
count = 1

i = 2
Character = c
Vowel? NO
count = 1

First window completed.

low = 0
high = 2
count = 1
max_vowel = 1

==========================================================
WHILE LOOP - ITERATION 1
==========================================================

Current Window = [a b c]

Before removing
low = 0
high = 2
count = 1

Remove:
s[low] = a
Vowel? YES
count = 0

Move pointers
low = 1
high = 3

Add:
s[high] = i
Vowel? YES
count = 1

Update answer
max_vowel = max(1,1) = 1

Current Window = [b c i]

State:
low = 1
high = 3
count = 1
max_vowel = 1

==========================================================
WHILE LOOP - ITERATION 2
==========================================================

Current Window = [b c i]

Before removing
low = 1
high = 3
count = 1

Remove:
s[low] = b
Vowel? NO
count = 1

Move pointers
low = 2
high = 4

Add:
s[high] = i
Vowel? YES
count = 2

Update answer
max_vowel = max(1,2) = 2

Current Window = [c i i]

State:
low = 2
high = 4
count = 2
max_vowel = 2

==========================================================
WHILE LOOP - ITERATION 3
==========================================================

Current Window = [c i i]

Before removing
low = 2
high = 4
count = 2

Remove:
s[low] = c
Vowel? NO
count = 2

Move pointers
low = 3
high = 5

Add:
s[high] = i
Vowel? YES
count = 3

Update answer
max_vowel = max(2,3) = 3

Current Window = [i i i]

State:
low = 3
high = 5
count = 3
max_vowel = 3

==========================================================
WHILE LOOP - ITERATION 4
==========================================================

Current Window = [i i i]

Before removing
low = 3
high = 5
count = 3

Remove:
s[low] = i
Vowel? YES
count = 2

Move pointers
low = 4
high = 6

Add:
s[high] = d
Vowel? NO
count = 2

Update answer
max_vowel = max(3,2) = 3

Current Window = [i i d]

State:
low = 4
high = 6
count = 2
max_vowel = 3

==========================================================
WHILE LOOP - ITERATION 5
==========================================================

Current Window = [i i d]

Before removing
low = 4
high = 6
count = 2

Remove:
s[low] = i
Vowel? YES
count = 1

Move pointers
low = 5
high = 7

Add:
s[high] = e
Vowel? YES
count = 2

Update answer
max_vowel = max(3,2) = 3

Current Window = [i d e]

State:
low = 5
high = 7
count = 2
max_vowel = 3

==========================================================
WHILE LOOP - ITERATION 6
==========================================================

Current Window = [i d e]

Before removing
low = 5
high = 7
count = 2

Remove:
s[low] = i
Vowel? YES
count = 1

Move pointers
low = 6
high = 8

Add:
s[high] = f
Vowel? NO
count = 1

Update answer
max_vowel = max(3,1) = 3

Current Window = [d e f]

State:
low = 6
high = 8
count = 1
max_vowel = 3

==========================================================
LOOP ENDS
==========================================================

Condition:
high < len(s)-1

8 < 8

False

Return:

max_vowel = 3




TIME COMPLEXITY :
O(n)

SPACE COMPLEXITY:
O(1)



"""