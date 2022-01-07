"""
2.Write a program which accept N numbers from user and store it into List. Return Maximum 
number from that List. 
Input : Number of elements : 7 
Input Elements : 13 5 45 7 4 56 34 
Output : 56 
"""

def Max(Arr):
	i=0
	iMax=Arr[i]
	for i in range(len(Arr)):
		if(iMax<Arr[i]):
			iMax=Arr[i]
	return iMax

def main():
	iLength=0
	Data=[]
	iRet=0

	print("Enter number of elements in the list are: ")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Data.append(int(input()))

	iRet=Max(Data)
	print("Maximum number from list are: ",iRet)

if __name__=="__main__":
	main()