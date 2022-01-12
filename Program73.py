
def CheckPerfect(iNo):
	iSum=0

	for i in range(1,iNo):
		if((iNo%i)==0):
			iSum=iSum+i

	if(iSum==iNo):
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
		print(iValue,"is a Perfect Number")

	else:
		print(iValue,"is not a perfect number")


if __name__=="__main__":
	main()