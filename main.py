#Factorial: 5! = 5 * 4 * 3 * 2 * 1

#Define a variable that does a factorial of some number x
def factorial(x):
    
    total = 1
    
    for i in range(1, x + 1):
        total = total * i 

    return total 

#print the funtion in order to test it
print (factorial(1000))
