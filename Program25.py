"""
5.Write a program which accept N numbers from user and store it into List. Return addition of all 
prime numbers from that List. Main python file accepts N numbers from user and pass each 
number to ChkPrime() function which is part of our user defined module named as 
MarvellousNum. Name of the function from main python file should be ListPrime(). 
Input : Number of elements : 11 
Input Elements : 13 5 45 7 4 56 10 34 2 5 8 
Output : 32 (13 + 5 + 7 +2 + 5)
"""

def ChkPrime(Brr):
	iSum=0
	for i in range(len(Brr)):
		Bflag=True
		for j in range(2,Brr[i]):
			if((Brr[i]%j)==0):
				Bflag=False
				break
		if(Bflag==True):
			iSum=iSum+Brr[i]
	return iSum
	
def main():
	iLength=0
	Arr=[]

	print("Enter the number of elements in the list are:")
	iLength=int(input())

	print("Enter elements")
	for i in range(iLength):
		Arr.append(int(input()))

	iRet=ChkPrime(Arr)
	print("Addition of All prime numbers are :",iRet)

if __name__=="__main__":
	main()