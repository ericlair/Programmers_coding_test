import math
import fractions

def solution(numer1, denom1, numer2, denom2):
    
    a = numer1*denom2 + numer2*denom1
    b = denom1*denom2
    
    g = math.gcd(a,b)
    
    a //= g
    b //= g
    
    
    #---------------------------------------------------
    
    ans = fractions.Fraction(numer1,denom1) + fractions.Fraction(numer2,denom2)
    a = ans.numerator
    b = ans.denominator
    
    
    answer = [a, b]
    return answer