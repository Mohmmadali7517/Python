
def SumFactors(iNo):
	iSum=0
	for i in range(1,iNo):
		if((iNo%i)==0):
			iSum=iSum+i

	return iSum

def CheckPerfect(iNo):
	iResult=0
	iResult=SumFactors(iNo)
	if(iResult==iNo):
		return True
	else:
		return False

def main():
	iValue=0
	bret=False

	print("Enter Number")
	iValue=int(input())

	bret=CheckPerfect(iValue)

	if(bret==True):
		print(iValue,"is Perfect number")

	else:
		print(iValue,"is not a perfect number")

if __name__=="__main__":
	main()