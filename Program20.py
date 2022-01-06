#10. Write a program which accept number from user and return addition of digits in that number. 
#Input : 5187934 Output : 37

def SumDigits(iValue):
	iSum,idigit=0,0

	while(iValue!=0):
		idigit=iValue%10
		iSum=iSum+idigit
		iValue=int(iValue/10)
	return iSum

def main():
	iValue=0
	print("Enter number")
	iValue=int(input())

	iRet=SumDigits(iValue)
	print("Sum of digits are : ",iRet)

if __name__ == '__main__':
	main()