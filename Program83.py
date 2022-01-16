
def Minimum(iNo1,iNo2):
	iResult=0
	if(iNo1<iNo2):
		iResult=iNo1

	elif(iNo2<iNo1):
		iResult=iNo2

	return iResult
	
def main():
	iValue1,iValue2=0,0

	print("Enter First number")
	iValue1=int(input())

	print("Enter Second number")
	iValue2=int(input())

	iRet=Minimum(iValue1,iValue2)
	print("Minimum number is : ",iRet)

if __name__=="__main__":
	main()