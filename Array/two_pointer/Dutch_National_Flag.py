def Dutch_National_Flag(colors):
    low=0 
    mid=0
    n=len(colors)
    high=n-1

    while mid<=high:
        if colors[mid]==0:
            temp=colors[mid]
            colors[mid]=colors[low]
            colors[low]=temp 
            low+=1
            mid+=1
        elif colors[mid]==1:
            mid+=1
        else:
            temp=colors[mid]
            colors[mid]=colors[high]
            colors[high]=temp 
            high-=1 
    return colors

if __name__== "__main__":
    colors=[1,2,0,1,2,0]
    print(Dutch_National_Flag(colors))



"""

Dutch National Flag – Revision Notes:

Why don't we do mid++ after swapping with high?

The element coming from high is unprocessed (unknown). It could be 0, 1, or 2, so we must check it again. Therefore, don't increment mid.

Why do we do mid++ after swapping with low?

The element coming from low is already processed, so no need to check it again. Therefore, increment mid.

Memory Trick
Swap with low → Processed element → mid++ ✅
Swap with high → Unknown element → Don't mid++ ❌


"""

