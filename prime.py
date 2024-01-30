lower=int(input("Enter the lower limit:"))
upper=int(input("Enter the upper limit:"))
print("the prime numbers in between",lower,"and",upper,"are:")
for n in range (lower,upper+1):
   if n>1:
     for i in range (2,n):
       if (n%i==0):
	           break
     else:
      print(n)
