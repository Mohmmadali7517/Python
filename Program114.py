
def LastOccurance(Brr,iSearch):
	i=0
	index=-1
	while(i!=len(Brr)):
		if(Brr[i]==iSearch):
			index=i
		i+=1
	return index
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