"""1. Write a recursive program which display below pattern.
Input : 5
Output : * * * * *
"""

def Display(i):

	if(i>0):
		print("*\t",end='')
		i-=1
		Display(i)

def main():
	iNo=0
	print("Enter number to display")
	iNo=int(input())
	Display(iNo)

if __name__=="__main__":
	main()