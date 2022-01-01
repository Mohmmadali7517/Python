#10. Write a program which accept name from user and display length of its name. 
#Input : Marvellous Output : 10

def main():
	print("Enter name")
	iName=str(input())

	iRet=str(len(iName))

	print("length of string is :",iRet)
	
if __name__=="__main__":
	main()