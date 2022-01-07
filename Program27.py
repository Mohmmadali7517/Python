#2.Write a program which contains one lambda function which accepts two parameters and return its multiplication. 
#Input : 4 3 Output : 12 
#Input : 6 3 Output : 18 

Mult=lambda a,b:a*b

def main():
	iNo1,iNo2=0,0

	print("Enter number1")
	iNo1=int(input())

	print("Enter number2")
	iNo2=int(input())

	iRet=Mult(iNo1,iNo2)
	print("Multiplication is :",iRet)

if __name__=="__main__":
	main()