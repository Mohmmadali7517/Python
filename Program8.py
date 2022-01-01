#8. Write a program which accept number from user and print that number of “*” on screen. 
#Input : 5 Output : * * * * *

def Display(iValue):
	for i in range(iValue):
		print("*\t",end='')
def main():
	iValue=0

	print("Enter number to display")
	iValue=int(input())

	Display(iValue)

if __name__=="__main__":
	main()