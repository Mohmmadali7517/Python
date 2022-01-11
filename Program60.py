
def Display():
	iNo=7521
	iDigit=0

	iDigit=iNo%10
	print(int(iDigit))
	iNo=iNo/10

	iDigit=iNo%10
	print(int(iDigit))
	iNo=iNo/10
	
	iDigit=iNo%10
	print(int(iDigit))
	iNo=iNo/10
	
	iDigit=iNo%10
	print(int(iDigit))
	iNo=iNo/10

def main():
	Display()


if __name__=="__main__":
	main()