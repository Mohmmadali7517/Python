"""3.Write a recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1
"""

def Display(i):
	if(i>0):
		print(i,end='\t')
		i-=1
		Display(i)

def main():
	iNo=0
	print("Enter number")
	iNo=int(input())

	Display(iNo)

if __name__=="__main__":
	main()