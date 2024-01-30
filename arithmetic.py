num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
operation=input("choose an arithmetic operation(+,_,*,/,** for exponentiation,// for floor division and % for modulo):")
if operation=="+":
	result=num1+ num2
elif operation=="-":
	result=num1- num2
elif operation=="*":
	result=num1* num2
elif operation=="/":
	result=num1/num2
elif operation=="//":
	result=num1// num2
elif operation=="**":
	resut=num1** num2
elif operation=="%":
	result=num1% num2
else :
	 print(" invalid input")
print("The result of the arithmetic operation is :",result)
