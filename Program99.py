
def Addition(Brr):
	iSum=0
	for i in range(len(Brr)):
		iSum=iSum+Brr[i]
	return iSum
	
def main():
	Arr=[]
	iRet=0
	iLength=0

	print("Enter number of elements ")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))
	iRet=Addition(Arr)
	print("Addition is :",iRet)

if __name__=="__main__":
	main()