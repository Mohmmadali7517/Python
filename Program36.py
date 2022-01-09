"""3. Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.
"""

class Numbers:

	def __init__(self,a):
		self.Value=a 

	def ChkPrime(self):
		bFlag=True
		for i in range(2,self.Value):
			if((self.Value%i)==0):
				bFlag=False
				break
		return bFlag

	def Factors(self):
		for i in range(1,self.Value):
			if((self.Value%i)==0):
				print(i,end="\t")
		print()

	def ChkPerfect(self):
		iNo=self.Value
		iSum=0

		for i in range(1,self.Value):
			if((self.Value%i)==0):
				iSum=iSum+i
		if(iSum==iNo):
			return True
		else:
			return False

	def SumFactors(self):
		iSum=0
		for i in range(1,self.Value):
			if((self.Value%i)==0):
				iSum=iSum+i 
		return iSum

def main():

	print("Enter Number")
	iValue=int(input())

	obj=Numbers(iValue)
	bRet=obj.ChkPrime()
	if(bRet==True):
		print(iValue," is prime number")
	else:
		print(iValue," is not prime number")

	obj.Factors()

	bRet=obj.ChkPerfect()
	if(bRet==True):
		print(iValue," is Perfect Number")
	else:
		print(iValue," is Not Perfect Number")

	iRet=obj.SumFactors()
	print("Sum of Factors of",iValue," is : ",iRet)

if __name__=="__main__":
	main()

