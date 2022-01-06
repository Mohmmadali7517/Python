#3. Write a program which accept one number from user and return its factorial.
#Input : 5 Output : 120 

def Fact(iNo):
	iMult=1
	for i in range(1,iNo+1):
		iMult=i*iMult

	return iMult;

def main():
	iValue=0

	print("Enter number :")
	iValue=int(input())

	iRet=Fact(iValue)
	print("Factorial is : ",iRet)

if __name__ == '__main__':
	main()