def bag_of_tokens(tokens,power):
    left=0
    right=len(tokens)-1
    tokens.sort()
    score=0
    max_score=0

    while left<=right:
        if tokens[left]<=power:
            power-=tokens[left]
            score=score+1
            max_score=max(score,max_score)
            
            left+=1
        if power<tokens[left] and score>0:
            power+=tokens[right]
            score=score-1
            max_score=max(score,max_score)
            
            right-=1
        else:
            break
    return max_score