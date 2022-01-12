
def Power(x,y):
	iMult=1

	for i in range(1,y+1):
		iMult=iMult*x

	return iMult

def main():
	iValue1,iValue2=0,0

	print("Enter base number")
	iValue1=int(input())

	print("Enter Power")
	iValue2=int(input())

	iRet=Power(iValue1,iValue2)

	print(iValue1,"to Power",iValue2,"is :",iRet)

if __name__=="__main__":
	main()