
def CountDigit(iNo):
	idigit=0
	iCnt=0
	while(iNo!=0):
		idigit=iNo%10
		if(idigit>=5):
			iCnt+=1
		iNo=iNo/10
	return iCnt
	
def main():
	iValue=0
	print("Enter number")
	iValue=int(input())

	iRet=CountDigit(iValue)
	print("Digits greater than 5 are :",iRet)

if __name__=="__main__":
	main()