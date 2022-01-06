#4.Write a program which accept one number form user and return addition of its factors. 
#Input : 12 Output : 16 (1+2+3+4+6)

def FactSum(iNo):
	iSum=0
	for i in range(1,iNo):
		if((iNo%i)==0):
			iSum=iSum+i

	return iSum
		
def main():
	iValue=0

	print("Enter number")
	iValue=int(input())

	iRet=FactSum(iValue)
	print("Sum of factors is : ",iRet)

if __name__ == '__main__':
	main()