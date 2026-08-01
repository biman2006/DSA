"""
Algorithm:
low=0
high=0
freq={}
res=-1

for high (0->len(nums)):
  freq[nums[high]]=freq.get(nums[high],0)+1
  while len(freq)>2:
    freq[nums[low]]-=1

    if freq[nums[low]]==0:
       del freq[nums[low]] from freq
    low++
  if len(freq)<=2:
    length=high-low+1
    if length>res:
      res=length
return the res
      
   

"""

# CODE:

def fruit_basket(nums,k):
    low=0
    high=0
    freq={}
    res=-1

    for high in range(len(nums)):
        freq[nums[high]]=freq.get(nums[high],0)+1
        while (len(freq)>2):
            freq[nums[low]]-=1
            if freq[nums[low]]==0:
                del freq[nums[low]]
            low+=1
        if len(freq)<=2:
            length=high-low+1 
            if length>res:
                res=length 
    return res 

if __name__=="__main__":
    nums=[1,1,2,2,3,4]
    k=2 
    print(fruit_basket(nums,k))