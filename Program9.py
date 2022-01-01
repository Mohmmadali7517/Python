#9. Write a program which display first 10 even numbers on screen. 
#Output : 2 4 6 8 10 12 14 16 18 20

def Display(iValue):	
	for i in range(1,iValue+1):
		print(i*2,"\t",end='')

def main():
	iValue=0;
	print("Enter the number to display even number on screen")
	iValue=int(input())

	Display(iValue)

if __name__=="__main__":
	main()