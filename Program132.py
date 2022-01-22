def SmallCount(Brr):
	iCnt=0
	for i in range(len(Brr)):
		if((Brr[i]>='a')and(Brr[i]<='z')):
			iCnt+=1
	return iCnt

def main():
	Arr='\0'
	iRet=0

	print("Enter string")
	Arr=str(input())

	iRet=SmallCount(Arr)
	print("Small characters in string are :",iRet)

if __name__=="__main__":
	main()