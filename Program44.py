# Accept number from user and display that number of * on screen.
# Input : 4
# Output : *   *   *   *  

def Display(iNo):
	iCnt=1
	for iCnt in range(0,iNo):
		print("*\t",end='')
		

def main():
	print("Enter the number")
	iValue=int(input())

	Display(iValue)

if __name__=="__main__":
	main()
