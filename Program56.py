
def Factorial(iValue):
	iFact,iCnt=1,0

	if(iValue<0):
		iValue=-iValue

	for iCnt in range(1,iValue+1):
		iFact=iFact*iCnt

	return iFact

def main():
	iNo,iRet=0,0

	print("Enter Number")
	iNo=int(input())

	iRet=Factorial(iNo)

	print("Factorial is : ",iRet)


if __name__=="__main__":
	main()
