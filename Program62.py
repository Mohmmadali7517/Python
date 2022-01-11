
def Display(iValue):
	iDigit=0
	while(iValue!=0):
		iDigit=iValue%10
		print(iDigit,"\t",end='')
		iValue=int(iValue/10)

def main():
	iNo=0

	print("Enter number")
	iNo=int(input())

	Display(iNo)

if __name__=="__main__":
	main()