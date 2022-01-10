# Accept number from user and display that number of * on screen.
# Input : 4
# Output : *   *   *   *  

def Display(iNo):
	iCnt=1
	while(iCnt<=iNo):
		print("*\t",end='')
		iCnt=iCnt+1


def main():
	print("Enter the number")
	iValue=int(input())

	Display(iValue)

if __name__=="__main__":
	main()
