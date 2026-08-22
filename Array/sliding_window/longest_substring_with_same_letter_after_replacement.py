"""
ALGORITHM:

low=0
high=0
freq={}
max_freq=0
res=0

high (0-len(nums)):
   strore string[high] in freq 
   calculate max_freq=max(fre(string[high]),max_freq)
   calculate window_size=high-low+1

if window_size-max_freq>k: 
   shrink window(low++)
else:
   length-high-low+1
   res=max(res,length)
return res 




"""


def longest_substring_with_replacement_repeating_character(string,k):
    low=0
    high=0
    freq={}
    max_len=0
    max_freq=0
    
    for high in range(len(string)):
      freq[string[high]]=freq.get(string[high],0)+1
      window_size=high-low+1
      if freq[string[high]]>max_freq:
         max_freq=freq[string[high]]
      replacementNeeded=window_size-max_freq

      if replacementNeeded>k:
         freq[string[low]]-=1
         low+=1
      length=high-low+1
      if length>max_len:
         max_len=length
    return max_len
            


if __name__=="__main__":
    string="AABABBA"
    k=1
    print(longest_substring_with_replacement_repeating_character(string,k))



"""

DRY RUN:


---------------------------------------------------------------------------------------------------------------
Step | high | Char | Window  | Frequency         | Max_Freq | Window_Size | Replace | Action      | Answer
---------------------------------------------------------------------------------------------------------------
0    |  -   |  -   | ""      | {}                |    0     |      0      |    0    | Start       | 0
---------------------------------------------------------------------------------------------------------------
1    |  0   |  A   | A       | A=1               |    1     |      1      | 1-1=0   | Valid       | 1
---------------------------------------------------------------------------------------------------------------
2    |  1   |  A   | AA      | A=2               |    2     |      2      | 2-2=0   | Valid       | 2
---------------------------------------------------------------------------------------------------------------
3    |  2   |  B   | AAB     | A=2 B=1           |    2     |      3      | 3-2=1   | Valid       | 3
---------------------------------------------------------------------------------------------------------------
4    |  3   |  A   | AABA    | A=3 B=1           |    3     |      4      | 4-3=1   | Valid       | 4
---------------------------------------------------------------------------------------------------------------
5    |  4   |  B   | AABAB   | A=3 B=2           |    3     |      5      | 5-3=2   | Shrink      | 4
      Remove Left:
      Remove 'A'
      low = 1
      Window = ABAB
      Frequency = A=2 B=2
---------------------------------------------------------------------------------------------------------------
6    |  5   |  B   | ABABB   | A=2 B=3           |    3     |      5      | 5-3=2   | Shrink      | 4
      Remove Left:
      Remove 'A'
      low = 2
      Window = BABB
      Frequency = A=1 B=3
---------------------------------------------------------------------------------------------------------------
7    |  6   |  A   | BABBA   | A=2 B=3           |    3     |      5      | 5-3=2   | Shrink      | 4
      Remove Left:
      Remove 'B'
      low = 3
      Window = ABBA
      Frequency = A=2 B=2
---------------------------------------------------------------------------------------------------------------

Final Answer = 4



TIME COMPLEXITY:

O(n)

SPACE COMPLEXITY:
O(1)



"""
