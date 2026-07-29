def kids_candies(candies:list[int], extraCandies:int)->list[int]:
    max_candies=max(candies)

    result=[]

    for candy in candies:
        if candy+extraCandies>=max_candies:
            result.append(True)

        else:
            result.append(False)
    return result

if __name__=="__main__":
    candies=[2,3,5,1,3,0]
    extraCandies=3

    res=kids_candies(candies,extraCandies)
    print(res)

