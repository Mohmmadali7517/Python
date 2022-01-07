"""1.Write a program which accept N numbers from user and store it into List. Return addition of all 
elements from that List. 
Input : Number of elements : 6 
Input Elements : 13 5 45 7 4 56 
Output : 130
"""

def Addition(Arr):
	iSum=0
	for i in range(len(Arr)):
		iSum=iSum+Arr[i]

	return iSum

def main():
	iLength=0
	Data=[]
	iRet=0

	print("Enter the number of elements in list")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Data.append(int(input()))

	iRet=Addition(Data)
	print("Addition in list are : ",iRet)

if __name__=="__main__":
	main()