
def DisplayTable(iNo):
	for i in range(1,11):
		print(i*iNo)

		
def main():
	iValue=0

	print("Enter Number")
	iValue=int(input())

	DisplayTable(iValue)

if __name__=="__main__":
	main()