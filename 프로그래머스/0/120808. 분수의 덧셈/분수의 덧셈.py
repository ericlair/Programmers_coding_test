def solution(numer1, denom1, numer2, denom2):

    ans1 = numer1*denom2 + numer2*denom1    
    ans2 = denom2*denom1   
    
    i = min(ans1,ans2) 
    
    while i > 1 and not(ans1%i==0 and ans2%i==0) :
        i -= 1
    
    ans1//=i
    ans2//=i
    
    answer = [ans1, ans2]
    
    return answer