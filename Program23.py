"""
3.Write a program which accept N numbers from user and store it into List. Return Minimum 
number from that List. 
Input : Number of elements : 4 
Input Elements : 13 5 45 7 
Output : 5 
"""

def Min(Brr):
	i=0
	iMin=Brr[i]
	for i in range(len(Brr)):
		if(Brr[i]<iMin):
			iMin=Brr[i]
	return iMin
	
def main():
	iLength=0
	Arr=[]
	iRet=0

	print("Enter number of lements in list are :")
	iLength=int(input())

	print("Enter Elements")
	for i in range(iLength):
		Arr.append(int(input()))

	iRet=Min(Arr)
	print("Minimum Element in the list is :",iRet)

if __name__=="__main__":
	main()