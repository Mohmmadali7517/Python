#5.Write a program which accept one number for user and check whether number is prime or not. 
#Input : 5 Output : It is Prime Number 

def CheckPrime(iNo):
	iSum=0
	for i in range(2,iNo):
		if((iNo%i)==0):
			iSum=iSum+i
	if(iSum==0):
		return True

def main():
	iValue=0
	print("Enter number")
	iValue=int(input())

	bret=CheckPrime(iValue)
	if(bret==True):
		print("It is Prime Number")
	else:
		print("It is not prime number")

if __name__=="__main__":
	main()