
def CheckEven(iValue):
	if((iValue%2)==0):
		return True
	else:
		return False
		
def main():
	iNo=0
	bret=False

	print("Enter number")
	iNo=int(input())

	bret=CheckEven(iNo)
	if(bret==True):
		print(iNo,"is even number")

	else:
		print(iNo,"is not even number")


if __name__=="__main__":
	main()