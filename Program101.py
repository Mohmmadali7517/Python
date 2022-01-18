
def CountEven(Brr):
	iCnt=0
	for i in range(len(Brr)):
		if((Brr[i]%2)==0):
			iCnt+=1

	return iCnt
	
def main():
	Arr=[]
	iLength=0
	iRet=0

	print("Enter the number of elements ")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))

	iRet=CountEven(Arr)
	print("Even elements in List are :",iRet)

if __name__=="__main__":
	main()