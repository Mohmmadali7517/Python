"""5. Write a recursive program which accept number from user and return its
factorial.
Input : 5
Output : 120
"""

def Factorial(iNo):
	if(iNo==0):
		return 1
	return(iNo*Factorial(iNo-1))

def main():
	iNo=0;
	print("Enter number")
	iNo=int(input())
	iRet=Factorial(iNo)
	print("Factorial of {} is {}".format(iNo,iRet))

if __name__=="__main__":
	main()