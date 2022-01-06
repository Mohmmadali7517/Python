#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user.

import Arithmetic as A

def main():
	iNo1=0
	iNo2=0

	print("Enter first number")
	iNo1=int(input())

	print("Enter second number")
	iNo2=int(input())

	iRet=A.Add(iNo1,iNo2)
	print("Addition is :",iRet)
	iRet=A.Sub(iNo1,iNo2)
	print("Substraction is : ",iRet)
	iRet=A.Mult(iNo1,iNo2)
	print("Multiplication is : ",iRet)
	iRet=A.Div(iNo1,iNo2)
	print("Division is : ",iRet)

if __name__ == '__main__':
	main()