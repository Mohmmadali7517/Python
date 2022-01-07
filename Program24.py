"""
4.Write a program which accept N numbers from user and store it into List. Accept one another 
number from user and return frequency of that number from List. 
Input : Number of elements : 11 
Input Elements : 13 5 45 7 4 56 5 34 2 5 65 
Element to search : 5 
Output : 3 
"""

def CountFrequency(Brr,no):
	iCnt=0
	for i in range(len(Brr)):
		if(Brr[i]==no):
			iCnt+=1
	return iCnt

def main():
	iLength=0
	Arr=[]
	iSearch=0
	iRet=0

	print("Enter the elements in the list are: ")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))
	print("Enter the element to search ")
	iSearch=int(input())

	iRet=CountFrequency(Arr,iSearch)
	print("Frequency of element is:",iRet)

if __name__=="__main__":
	main()