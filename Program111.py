
def CheckNumber(Brr,iNo):
	bflag=False
	for i in range(len(Brr)):
		if(Brr[i]==iNo):
			bflag=True
			break
	return bflag
	
def main():
	iLength=0
	iSearch=0
	Arr=[]
	bRet=False

	print("Enter the number of elements")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))

	print("Enter the element to search")
	iSearch=int(input())

	bRet=CheckNumber(Arr,iSearch)
	if(bRet==True):
		print(iSearch,"number is there in list")
	else:
		print(iSearch,"number is not there in list")

if __name__=="__main__":
	main()