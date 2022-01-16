
def Display(iNo):
	for i in range(iNo,0,-1):
		print(i,"\t",end='')

def main():
	iValue=0

	print("Enter Number")
	iValue=int(input())

	Display(iValue)

if __name__=="__main__":
	main()