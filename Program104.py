
def CountRange(Brr):
	iCnt=0
	for i in range(len(Brr)):
		if((Brr[i]>10)and(Brr[i]<20)):
			iCnt+=1

	return iCnt

def main():
	iLength=0
	Arr=[]
	iRet=0

	print("Enter the number of elements ")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))
	iRet=CountRange(Arr)
	print("Elements in the range 10 to 20 are: ",iRet)

if __name__=="__main__":
	main()