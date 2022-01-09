"""2. Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount
from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects
"""

class BankAccount:
	
	ROI=10.5

	def __init__(self,a,b):
		self.Name=a 
		self.Amount=b

	def Deposit(self,a):
		self.Amount+=a 

	def Withdraw(self,a):
		self.Amount-=a

	def CalculateInterest(self):
		Interest=(self.Amount*self.ROI)/100
		print("Interest of that Amount is :",Interest)

	def Display(self):
		print("Name of account holder :",self.Name)
		print("Total Amount is :",self.Amount)

def main():
	obj1=BankAccount("Piyush",12500)
	obj1.Deposit(2500)
	obj1.Display()

	obj2=BankAccount("Chetan",25000)
	obj2.Withdraw(12500)
	obj2.Display()

	obj1.CalculateInterest()
	obj2.CalculateInterest()

if __name__=="__main__":
	main()