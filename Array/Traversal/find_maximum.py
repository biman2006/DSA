def runningSum(arr:list[int])->list[int]:
    for i in range(1,len(arr)):
        arr[i]+=arr[i-1]

    return arr 

if __name__=="__main__":
    arr=[1,2,3,4]

    result=runningSum(arr)
    print(result)