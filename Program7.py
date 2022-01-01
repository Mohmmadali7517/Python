#7. Write a program which contains one function that accept one number from user and returns
#true if number is divisible by 5 otherwise return false.
#Input : 8 Output : False
#Input : 25 Output : True

def CheckDiv(iValue):
	if((iValue%5)==0):
		return True
	else:
		return False

def main():
	iValue=0
	print("Enter number ")
	iValue=int(input())

	ret=CheckDiv(iValue)
	if(ret==True):
		print(iValue," is divisible by 5")
	else:
		print(iValue," is not divisible by 5")

if __name__=="__main__":
	main()