
def FirstOccurance(Brr,iNo):
	i=0
	while(i!=len(Brr)):
		if(Brr[i]==iNo):
			break
		i+=1
	if(i==len(Brr)):
		return -1
	else:
		return i

def main():
	iLength=0
	Arr=[]
	iRet=0
	iSearch=0

	print("Enter the number of elements in list")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))

	print("Enter the element to search")
	iSearch=int(input())

	iRet=FirstOccurance(Arr,iSearch)
	print("First occurance of the number at index number is :",iRet)

if __name__=="__main__":
	main()