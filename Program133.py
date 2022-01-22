def CountCapital(Brr):
	iCnt=0
	for i in range(len(Brr)):
		if((Brr[i]>='A')and(Brr[i]<='Z')):
			iCnt+=1
	return iCnt

def main():
	Arr='\0'
	iRet=0

	print("Enter String")
	Arr=str(input())

	iRet=CountCapital(Arr)
	print("Capital letters in String are :",iRet)

if __name__=="__main__":
	main()