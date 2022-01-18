
def SumOdd(Brr):
	iSum=0

	for i in range(len(Brr)):
		if((Brr[i]%2)!=0):
			iSum=iSum+Brr[i]
	return iSum

def main():
	Arr=[]
	iLength=0
	iRet=0

	print("Enter the number of elements ")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))

	iRet=SumOdd(Arr)
	print("Sum of odd elements are : ",iRet)

if __name__=="__main__":
	main()