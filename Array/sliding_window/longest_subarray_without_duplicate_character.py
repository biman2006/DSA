""" 
ALGORITHM:

low=0
high=0
freq={}
max_len=0

loop(hight 0 to len(strings)):
   freq[s[high]]=freq.get(nums[high],0)+1

   while frew[s[high]]>1:
     freq[s[low]]-=1
     low+=1
   max_len=max(max_len,high-low+1)

return max_len 
   """








def longest_subarray_without_duplicate_character(strings):
    low=0
    high=0
    n=len(strings)
    freq={}
    max_len=0
    for high in range(n):
        freq[strings[high]]=freq.get(strings[high],0)+1

        while freq[strings[high]]>1:
            freq[strings[low]]-=1
            low+=1
        max_len=max(max_len,high-low+1)

    return max_len


if __name__=="__main__":
    strings="abcabcbb"
    print(longest_subarray_without_duplicate_character(strings))



    """

    DRY RUN : Longest Substring Without Repeating Characters
Input : "abcabcbb"

--------------------------------------------------------------------------------------------
Step | high | s[high] | Action                     | low | Window | freq              | max_len
--------------------------------------------------------------------------------------------
Start|  -   |    -    | Initialize                 |  0  | ""     | {}                | 0
--------------------------------------------------------------------------------------------
1    |  0   |    a    | Add 'a'                    |  0  | a      | {a:1}             | 1
--------------------------------------------------------------------------------------------
2    |  1   |    b    | Add 'b'                    |  0  | ab     | {a:1,b:1}         | 2
--------------------------------------------------------------------------------------------
3    |  2   |    c    | Add 'c'                    |  0  | abc    | {a:1,b:1,c:1}     | 3
--------------------------------------------------------------------------------------------
4    |  3   |    a    | Add 'a' (Duplicate)        |  0  | abca   | {a:2,b:1,c:1}     | 3
4.1  |  -   |    -    | Remove 'a', low++          |  1  | bca    | {a:1,b:1,c:1}     | 3
--------------------------------------------------------------------------------------------
5    |  4   |    b    | Add 'b' (Duplicate)        |  1  | bcab   | {a:1,b:2,c:1}     | 3
5.1  |  -   |    -    | Remove 'b', low++          |  2  | cab    | {a:1,b:1,c:1}     | 3
--------------------------------------------------------------------------------------------
6    |  5   |    c    | Add 'c' (Duplicate)        |  2  | cabc   | {a:1,b:1,c:2}     | 3
6.1  |  -   |    -    | Remove 'c', low++          |  3  | abc    | {a:1,b:1,c:1}     | 3
--------------------------------------------------------------------------------------------
7    |  6   |    b    | Add 'b' (Duplicate)        |  3  | abcb   | {a:1,b:2,c:1}     | 3
7.1  |  -   |    -    | Remove 'a', low++          |  4  | bcb    | {a:0,b:2,c:1}     | 3
7.2  |  -   |    -    | Remove 'b', low++          |  5  | cb     | {a:0,b:1,c:1}     | 3
--------------------------------------------------------------------------------------------
8    |  7   |    b    | Add 'b' (Duplicate)        |  5  | cbb    | {a:0,b:2,c:1}     | 3
8.1  |  -   |    -    | Remove 'c', low++          |  6  | bb     | {a:0,b:2,c:0}     | 3
8.2  |  -   |    -    | Remove 'b', low++          |  7  | b      | {a:0,b:1,c:0}     | 3
--------------------------------------------------------------------------------------------

Final Answer:
Longest Substring = "abc"
Length = 3
    
    
    
    
    """