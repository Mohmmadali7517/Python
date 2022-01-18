
def CheckNumber(Brr):
	bflag=False
	for i in range(len(Brr)):
		if(Brr[i]==11):
			bflag=True
			break
	return bflag

def main():
	iLength=0
	Arr=[]
	bRet=False

	print("Enter the number of elements")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))

	bRet=CheckNumber(Arr)
	if(bRet==True):
		print("11 Number is there")
	else:
		print("11 Number is not there")

if __name__=="__main__":
	main()