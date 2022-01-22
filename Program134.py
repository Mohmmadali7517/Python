def Count(Brr):
	cCount=0
	sCount=0

	for i in range(len(Brr)):
		if((Brr[i]>='A')and(Brr[i]<='Z')):
			cCount+=1

		elif((Brr[i]>='a')and(Brr[i]<='z')):
			sCount+=1
	return sCount,cCount

def main():
	Arr='\0'
	iRet1=0
	iRet2=0

	print("Enter string")
	Arr=str(input())

	iRet1,iRet2=Count(Arr)
	print("Small letters are in string are:",iRet1)
	print("Capital letters are in string are:",iRet2)

if __name__=="__main__":
	main()