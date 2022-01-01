#2. Write a program which contains one function named as ChkNum() which accept one
#parameter as number. If number is even then it should display “Even number” otherwise
#display “Odd number” on console.
#Input : 11 Output : Odd Number
#Input : 8 Output : Even Number

def ChkNum(iValue):
	if((iValue%2)==0):
		print("Your Entered number is even number")
	else:
		print("Your Entered number is odd number")
		
def main():
	iValue=0

	print("Enter number")
	iValue=int(input())

	ChkNum(iValue)

if __name__=="__main__":
	main()