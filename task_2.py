# code to determine if a number is a prime number
def test_prime(r):
	if (r==1):
	    return False
	elif (r==2):
	    return True;
	else:
	    for x in range(2,r):
	        if(r % x==0):
	            return False
	    return True             
print(test_prime(7))