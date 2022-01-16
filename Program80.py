
def DisplayEven(iNo):
	for i in range(1,iNo+1):
		print(i*2,"\t",end='')
		
def main():
	iValue=0

	print("Enter Number")
	iValue=int(input())

	DisplayEven(iValue)

if __name__ == "__main__":
	main()