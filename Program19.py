""" 
9. Write a program which accept number from user and return number of digits in that number. 
Input : 5187934 Output : 7
"""

def CountDigits(iNo):
	iCnt=0
	while(iNo!=0):
		iCnt+=1
		iNo=int(iNo/10)
	return iCnt

def main():
	iValue=0
	print("Enter number ")
	iValue=int(input())

	iRet=CountDigits(iValue)
	print("number of digits are : ",iRet)

if __name__=="__main__":
	main()