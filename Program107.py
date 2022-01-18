
def Min(Brr):
	i=0
	iMin=Brr[i]
	for i in range(len(Brr)):
		if(Brr[i]<iMin):
			iMin=Brr[i]
	return iMin
	
def main():
	iLength=0
	Arr=[]
	iRet=0

	print("Enter the number of elements")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))
	iRet=Min(Arr)
	print("Minimum number in List are :",iRet)

if __name__=="__main__":
	main()