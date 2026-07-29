def best_time_to_sell_buy_stock(nums):
    min_price=nums[0]
    max_profit=0

    for i in range(len(nums)):
        profit=nums[i]-min_price
        max_profit=max(profit,max_profit)
        min_price=min(min_price,nums[i])

    return max_profit


if __name__=="__main__":
    nums=[1,2,4,0,7,9]
    print(best_time_to_sell_buy_stock(nums))
