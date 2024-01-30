def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    if(n2==0):
      print("Divison is not possible")
    else:
      return n1/n2
def power(n1,n2):
    return n2**n1
def calculator(n1,op,n2):
    if op=='+':
      return addition(n1,n2)
    elif op=='-':
      return subtraction(n1,n2)
    elif op=='*':
      return multiplication(n1,n2)
    elif op=='/':
      return division (n1,n2)
    elif op=='**':
      return power(n1,n2)
    else:
      print("Enter a valid operator")
print("operators are:\n+ for addition\n- for subtraction\n* for multiplication\n/ for division\n** for power")
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
op=str(input("Enter the operation to perform:"))
result=calculator(n1,op,n2)
print("Result:",result)
    
