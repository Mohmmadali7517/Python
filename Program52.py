
def Display(iValue):
	i=0;

	if(iValue==0):
		print("Your Entered number is 0")
		return

	if(iValue<0):
		iValue=-iValue

	for i in range(1,iValue+1):
		print(i,"\t",end='')

def main():
	iNo=0

	print("Enter Number")
	iNo=int(input())


	Display(iNo)

if __name__=="__main__":
	main()