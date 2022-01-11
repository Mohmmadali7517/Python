
def Display():
	iNo=7521
	iDigit=0

	while(iNo!=0):
		iDigit=iNo%10
		print(iDigit,"\t",end='')
		iNo=int(iNo/10)

def main():
	Display()


if __name__=="__main__":
	main()