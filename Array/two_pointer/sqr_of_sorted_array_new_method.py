from typing import List
def square_of_sorted_array(nums:List[int])->List[int]:
    n=len(nums)
    neg=[]
    pos=[]

    for num in nums:
        if num<0:
            neg.append(num)
        else:
            pos.append(num)
    if len(neg)==0:
        return [x*x for x in pos]
    if len(pos)==0:
        res=[x*x for x in neg]
        res.reverse()
        return res
    neg=[x*x for x in neg][::-1]
    pos=[x*x for x in pos]
    n,m=len(neg),len(pos)
    res=[]
    i=j=0
    while i<n and j<m:
        if neg[i]<pos[j]:
            res.append(neg[i])
            i+=1
        else:
            res.append(pos[j])
            j+=1
    while i<n:
        res.append(neg[i])
        i+=1
    while j<m:
        res.append(pos[j])
        j+=1
    return res 

if __name__=="__main__":
    nums=[-4,-1,0,3,10]
    print(square_of_sorted_array(nums))


