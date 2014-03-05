def is_luhn_valid(n):
    if n >= 0:
        if getLength(n) % 2 == 0:
            return evenFunction(n, 1, 0) % 10 == 0
        else:
            return oddFunction(n, 0, 0) % 10 == 0
    else:
        return false
    
def getLength(n):
    return len(str(n))

def evenFunction(n, count, sum):
    div = n / 10
    rem = n % 10    
    if div == 0:
        return sum + checkProduct(rem * 2)   
    count += 1
    sum = evenFunction(div, count, sum)   
    if count % 2 != 0:
        return sum + checkProduct(rem * 2)    
    else :
        return sum + rem

    def oddFunction(n, count, sum):
    div = n / 10
    rem = n % 10    
    if div == 0:
        return sum + rem   
    count += 1
    sum = oddFunction(div, count, sum)   
    if count % 2 != 0:
        return sum + rem    
    else :
        return sum + checkProduct(rem * 2)
    
 def checkProduct(prod):
        if prod > 9:
            return (prod - 9)
        else:
            return prod
