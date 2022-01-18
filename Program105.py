
def Max(Brr):
	iMax=0
	for i in range(len(Brr)):
		if(Brr[i]>iMax):
			iMax=Brr[i]
	return iMax

def main():
	iLength=0
	Arr=[]
	iRet=0

	print("Enter the number of elements")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))
	iRet=Max(Arr)
	print("Maximum number in the list is:",iRet)

if __name__=="__main__":
	main()