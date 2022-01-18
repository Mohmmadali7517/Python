
def Diff(Brr):
	i=0
	iMin=Brr[0]
	iMax=Brr[0]
	iDiff=0
	for i in range(len(Brr)):
		if(Brr[i]>iMax):
			iMax=Brr[i]
		if(Brr[i]<iMin):
			iMin=Brr[i]
	iDiff=iMax-iMin
	return iDiff

def main():
	iLength=0
	Arr=[]
	iRet=0

	print("Enter number of elements in List")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))

	iRet=Diff(Arr)
	print("Difference of Maximum and minimum number in list is:",iRet)

if __name__=="__main__":
	main()