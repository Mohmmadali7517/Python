
def CheckNumber(Brr):
	i=0
	while(i!=len(Brr)):
		if(Brr[i]==11):
			break
		i+=1
	if(i==len(Brr)):
		return False
	else:
		return True

def main():
	iLength=0
	Arr=[]
	iRet=False

	print("Enter the number of elements")
	iLength=int(input())

	print("Enter numbers")
	for i in range(iLength):
		Arr.append(int(input()))
	iRet=CheckNumber(Arr)
	if(iRet==True):
		print("11 number is there")
	else:
		print("11 number is not there")

if __name__=="__main__":
	main()