def height_check(heights:list[int])->list[int]:
    expected=heights.copy()
    n=len(expected)

    for i in range(n):
        flag=0
        for j in range(n-i-1):
            if expected[j]>expected[j+1]:
                expected[j],expected[j+1]=expected[j+1],expected[j]
                flag=1
        if flag!=1:
            break 

    mismatch=0
    for i in range(n):
        if heights[i]!=expected[i]:
         mismatch+=1
    return mismatch


if __name__=="__main__":
    heights=[1,1,4,2,1,3]
    res=height_check(heights)
    print(res)