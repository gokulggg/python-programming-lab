class Bankaccount:
	def __init__(self):
		self.balance=0
	def deposit(self):
		amount=int(input("Enter the amount to be deposited:"))
		self.balance=self.balance+amount
		print("The deposited amount is:",self.balance)
	def withdraw(self):
		wamount=int(input("Enter the amount to be withdrawn:"))
		if self.balance>=wamount:
		   self.balance=self.balance-wamount
		else:
		     print("Insufficient amount")
	def display(self):
		print("The balance amount in the bank is:",self.balance)
object=Bankaccount()
object.deposit()
object.withdraw()
object.display()
