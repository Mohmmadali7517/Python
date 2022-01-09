"""
2. Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5
"""

def Display(i,j):

	if(i>0):
		print(j,end='\t')
		i-=1
		j+=1
		Display(i,j)


def main():
	print("Enter number")
	iNo=int(input())

	Display(iNo,1)

if __name__=="__main__":
	main()