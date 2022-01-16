
def Average(iNo1,iNo2,iNo3):
	iSum,iResult=0,0

	iSum=iNo1+iNo2+iNo3
	iResult=iSum/3

	return iResult
	
def main():
	iValue1,iValue2,iValue3,iRet=0,0,0,0

	print("Enter first number")
	iValue1=int(input())

	print("Enter Second number")
	iValue2=int(input())

	print("Enter third number")
	iValue3=int(input())

	iRet=Average(iValue1,iValue2,iValue3)
	print("Average is : ",iRet)

if __name__=="__main__":
	main()