
def Factorial(iNo):
	iFact,iCnt=1,1

	if(iNo<0):
		iNo=-iNo

	while(iCnt<=iNo):
		iFact=iFact*iCnt
		iCnt=iCnt+1
	return iFact

def main():
	iValue=0
	iRet=0

	print("Enter number ")
	iValue=int(input())

	iRet=Factorial(iValue)
	print("Factorial of",iValue,"is",iRet)


if __name__=="__main__":
	main()