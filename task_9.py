# function to find a palindrome
 

def isaPalindrome(s):

    return s == s[::-1]
 
 
# Driver code

s = "madam"

ans = isaPalindrome(s)
 

if ans:

    print("Yes")

else:

    print("No")