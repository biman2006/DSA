def Even_num_in_array(arr:list[int])->list[int]:
    temp=0
    


    for i in range(len(arr)):
      count=0

      while arr[i]>0:
         count+=1
         arr[i]=arr[i]//10
      if count%2==0:
         temp+=1 
    return temp

if __name__=="__main__":
   arr=[12,34,2,8]

   result=Even_num_in_array(arr)
   print(result)