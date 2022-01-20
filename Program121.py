
def Fun(Brr):
	return len(Brr)
	
def main():
	Arr=0
	iRet=0

	print("Enter string")
	Arr=str(input())

	iRet=Fun(Arr)
	print("Length of the string is:",iRet)

if __name__=="__main__":
	main()