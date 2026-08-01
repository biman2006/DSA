def longest_substring_with_k_distinct_character(string,k):
    low=0
    high=0
    n=len(string)
    res=float('-inf')
    freq={}

    for high in range(n):
        freq[string[high]]=freq.get(string[high],0)+1
        while(len(freq)>k):
            freq[string[low]]-=1
            if (freq[string[low]]==0):
                del freq[string[low]]
            low+=1
        if len(freq)==k:
            length=high-low+1
            res=max(length,res)
    return res 

if __name__=="__main__":
    string="aabacbebebe"
    k=1
    print(longest_substring_with_k_distinct_character(string,k))
                
