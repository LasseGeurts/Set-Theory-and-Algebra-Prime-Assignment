import math

def primecheck():
    number = 1
    
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(number) + 1)):
            if number % x == 0: 
                isprime = False
                break
        
        if isprime:
            print(number)
        
        number += 2
       
primecheck()