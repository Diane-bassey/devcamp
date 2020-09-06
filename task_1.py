# Python program to find out 
# Sum of elements at even and 
# odd index positions separately 

# Function to calculate Sum 
def SumEvenOdd(a, n): 
	even = 0
	odd = 0
	for i in range(n): 

		# Loop to find even and odd Sum 
		if i % 2 == 0: 
			even += a[i] 
		else: 
			odd += a[i] 
	
	print ("Even index positions sum ", even)
	print ("Odd index positions sum ", odd)

# main Function 

arr = [9, 2, 3, 4, 0, 5 ] 
n = len(arr) 

SumEvenOdd(arr, n) 


