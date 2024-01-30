lim=1000
n=int(input("How many prime numbers do you want?:"))
count=0
for i in range(1,lim):
 if count<n:
       if i>1:
          for j in range(2,i):
	  if(i%j==0):
		   break
          else:
	       print(i)
               count=count+1
