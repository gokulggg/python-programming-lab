def palindrome(n):
   temp=n
   rev=0
   while n>0:
      rem=n%10
      rev=rev*10+rem
      n=n//10
   return temp==rev
num=int(input("Enter the number:"))
if palindrome(num):
	print(num,"is a palindrome")
else:
	print(num,"is not a palindrome")
