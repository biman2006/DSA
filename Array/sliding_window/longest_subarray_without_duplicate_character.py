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