"""4.Write a recursive program which accept number from user and return
summation of its digits.
Input : 879
Output : 24
"""

def SumDigit( n ):
    if n == 0:
        return 0
    return (n % 10 + SumDigit(int(n / 10)))
 

def main():
	print("Enter number")
	iNo=int(input())
	iRet=SumDigit(iNo)
	print("Sum of digits of {} is".format(iNo),iRet)

if __name__=="__main__":
	main()