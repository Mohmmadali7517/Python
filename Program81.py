
def Display(iNo):
	for i in range(1,iNo+1):
		if((i%2)==0):
			print("#\t",end='')
		else:
			print("*\t",end='')
			
def main():
	iValue=0

	print("Enter Number")
	iValue=int(input())

	Display(iValue)

if __name__=="__main__":
	main()