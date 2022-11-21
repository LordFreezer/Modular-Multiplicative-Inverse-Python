# Recursion Based
def gcd(a, b):
    global x, y
    if (b == 0):
        x=1
        y=0
        return a 
    greatest_common_divisor = gcd(b, a % b)
    x1 = x 
    y1 = y 
    
    x = y1
    y = x1 - (a // b) * y1 # // divides and returns floor
    return greatest_common_divisor

def modInverse (a, m):
    greatest_common_divisor = gcd(a, m)
    if(greatest_common_divisor != 1):
        print("Mod Inverse does not exist")
    else: 
        inv = (x % m + m) % m 
        print("Inverse", inv)
    
print(modInverse(7, 60))
