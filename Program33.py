"""3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains two instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
"""

class Arithematic:

	def __init__(self):
		self.Value1=0
		self.Value2=0

	def Accept(self):
		print("Enter first number")
		self.Value1=int(input())
		print("Enter Second number")
		self.Value2=int(input())

	def Addition(self):
		iSum=self.Value1+self.Value2
		return iSum

	def Substraction(self):
		iDiff=self.Value1-self.Value2
		return iDiff

	def Multiplication(self):
		iMult=self.Value1*self.Value2
		return iMult

	def Division(self):
		iDiv=self.Value1/self.Value2
		return iDiv

def main():
	obj1=Arithematic()
	obj2=Arithematic()
	obj3=Arithematic()
	obj4=Arithematic()

	obj1.Accept()
	iRet=obj1.Addition()
	print("Addition is :",iRet)

	obj2.Accept()
	iRet=obj2.Substraction()
	print("Substraction is :",iRet)

	obj3.Accept()
	iRet=obj3.Multiplication()
	print("Multiplication is : ",iRet)

	obj4.Accept()
	iRet=obj4.Division()
	print("Division is : ",iRet)

if __name__ == '__main__':
	main()