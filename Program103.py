
def Count(brr):
	iCnt=0
	for i in range(len(brr)):
		if(brr[i]>10):
			iCnt+=1
	return iCnt

def main():
	Arr=[]
	iLength=0
	iRet=0

	print("Enter the number of elements in list are ")
	iLength=int(input())

	print("Enter Elements")
	for i in range(iLength):
		Arr.append(int(input()))

	iRet=Count(Arr)
	print("Elements greater than 10 in the list are :",iRet)

if __name__=="__main__":
	main()