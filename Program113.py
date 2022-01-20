
def LastOccurance(Brr,iSearch):
	i=len(Brr)-1
	while(i!=-1):
		if(Brr[i]==iSearch):
			break
		i-=1
	if(i==-1):
		return -1
	else:
		return i

def main():
	iLength=0
	Arr=[]
	iRet=0
	iSearch=0

	print("Enter number of elements in list")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))
	print("Enter the number to search")
	iSearch=int(input())

	iRet=LastOccurance(Arr,iSearch)
	print("Last occurance of the number at index number is :",iRet)

if __name__=="__main__":
	main()