"""

ALGORITHM:

Algorithm

1. Create a frequency map of the pattern.

2. Create an empty frequency map for the window.

3. Initialize:
      left = 0
      result = []

4. Move the right pointer through the string.

5. Add s[right] to the window frequency.

6. If window size > len(pattern):
      • Remove s[left] from the window frequency.
      • If its frequency becomes 0, delete it.
      • Move left by 1.

7. If window frequency == pattern frequency:
      • Store left in the result.

8. Repeat until right reaches the end.

9. Return the result.




"""

def findanagram(string,p):
    if len(p)>len(string):
        return []

    pattern_freq={}
    window_freq={}

    for ch in p:
        pattern_freq[ch] = pattern_freq.get(ch,0)+1

    low=0
    high=0
    res=[]
    for high in range(len(string)):
        window_freq[string[high]] = window_freq.get(string[high],0)+1

        if high-low+1>len(p):
            window_freq[string[low]]-=1

            if window_freq[string[low]]==0:
                del window_freq[string[low]]
            low+=1

        if window_freq==pattern_freq:
            res.append(low)

    return res 


if __name__=="__main__":
    string="cbaebabacd"
    p="bac"

    print(findanagram(string,p))


"""
DRY RUN:


s = "cbaebabacd"
p = "abc"

Pattern Frequency
-----------------
{'a':1, 'b':1, 'c':1}

Window 1 = "cba"

Window Frequency
{'c':1,'b':1,'a':1}

Equal ✅
Answer = [0]

------------------------------------------------

Window 2 = "bae"

Remove c
Add e

Window Frequency
{'b':1,'a':1,'e':1}

Not Equal ❌

------------------------------------------------

Window 3 = "aeb"

Remove b
Add b

Window Frequency
{'a':1,'e':1,'b':1}

Not Equal ❌

------------------------------------------------

Window 4 = "eba"

Remove a
Add a

Window Frequency
{'e':1,'b':1,'a':1}

Not Equal ❌

------------------------------------------------

Window 5 = "bab"

Remove e
Add b

Window Frequency
{'b':2,'a':1}

Not Equal ❌

------------------------------------------------

Window 6 = "aba"

Remove b
Add a

Window Frequency
{'b':1,'a':2}

Not Equal ❌

------------------------------------------------

Window 7 = "bac"

Remove a
Add c

Window Frequency
{'b':1,'a':1,'c':1}

Equal ✅
Answer = [0,6]


TIME COMPLEXITY:
O(n)
SPACE COMPLEXITY:
O(1)

"""

