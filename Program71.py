
def Reverse(iInput):
	idigit,iRev=0,0

	while(iInput!=0):
		idigit=iInput%10
		iRev=(iRev*10)+idigit
		iInput=int(iInput/10)

	return iRev

def CheckPallindrome(iNo):
	iCheck=0
	iCheck=Reverse(iNo)

	if(iNo==iCheck):
		return True

	else:
		return False

def main():
	Value=0
	bret=False

	print("Enter Number")
	Value=int(input())

	bret=CheckPallindrome(Value)

	if(bret==True):
		print(Value,"is a pallindrome number")

	else:
		print(Value,"is not a pallindrome number")


if __name__=="__main__":
	main()