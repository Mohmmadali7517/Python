
def Addition(Brr):
	i,iSum=0,0

	for i in range(5):
		iSum=iSum+Brr[i]
	return iSum

def main():
	Arr=[]
	iRet,i=0,0

	print("Enter elements")
	for i in range(5):
		Arr.append(int(input()))

	iRet=Addition(Arr)
	print("Addition is : ",iRet)	

if __name__=="__main__":
	main()