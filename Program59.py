
def DisplayFactors(iValue):
	iCnt=0
	for iCnt in range(1,iValue):
		if((iValue%iCnt)==0):
			print(iCnt,"\t",end='')


def main():
	iNo=0

	print("Enter number")
	iNo=int(input())

	DisplayFactors(iNo)

if __name__=="__main__":
	main()