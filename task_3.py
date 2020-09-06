#  A school method based Python3 program  
# to check if a number is prime 
  
# function check whether a number  
# is prime or not 
def isaPrime(n): 
      
    # Corner case 
    if (n <= 1): 
        return False
  
    # Check from 2 to n-1 
    for i in range(2, n): 
        if (n % i == 0): 
            return False
  
    return True
  
# main Program to run code
if isaPrime(5): 
    print ("true") 
else: 
    print ("false") 
      