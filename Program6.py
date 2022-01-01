#6.Write a program which accept number from user and check whether that number is positive or
#negative or zero.
#Input : 11 Output : Positive Number
#Input : -8 Output : Negative Number
#Input : 0 Output : Zero

def CheckNumber(iValue):
	if(iValue>0):
		print("Your entered number is positive number ")
	elif(iValue<0):
		print("Your entered number is negative number ")
	elif(iValue==0):
		print("Your entered number is zero")
		
def main():
	iValue=0
	print("Enter number ")
	iValue=int(input())

	CheckNumber(iValue)

if __name__=="__main__":
	main()