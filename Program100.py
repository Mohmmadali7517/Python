
def Average(Brr):
	iSum=0
	iAverage=0

	for i in range(len(Brr)):
		iSum=iSum+Brr[i]

	iAverage=iSum/len(Brr)

	return iAverage

def main():
	Arr=[]
	iLength=0
	iRet=0

	print("Enter the number of elements")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))

	iRet=Average(Arr)
	print("Average is : ",iRet)

if __name__=="__main__":
	main()