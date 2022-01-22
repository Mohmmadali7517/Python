def SpaceCount(Arr):
	iCnt=0
	for i in range(len(Arr)):
		if(Arr[i]==' '):
			iCnt+=1
	return iCnt

def main():
	ch='\0'
	iRet=0

	print("Enter string")
	ch=str(input())

	iRet=SpaceCount(ch)
	print("number of space in string are :",iRet)

if __name__=="__main__":
	main()