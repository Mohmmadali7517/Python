
def DigitSum(iValue):
	iDigit,iSum=0,0
	while(iValue!=0):
		iDigit=iValue%10
		iSum=iSum+iDigit
		iValue=int(iValue/10)
	return iSum

def main():
	iNo,iRet=0,0

	print("Enter number")
	iNo=int(input())

	iRet=DigitSum(iNo)
	print("Sum of digits are :",iRet)

if __name__=="__main__":
	main()