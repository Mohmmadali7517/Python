
def Addition(iValue):
	iSum,iCnt=0,0
	if(iValue<0):
		iValue=-iValue

	for iCnt in range(1,iValue+1):
		iSum=iSum+iCnt
	return iSum


def main():
	iNo,iRet=0,0

	print("Enter Number")
	iNo=int(input())

	iRet=Addition(iNo)

	print("Addition is : ",iRet)

if __name__=="__main__":
	main()