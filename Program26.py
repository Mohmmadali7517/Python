#1.Write a program which contains one lambda function which accepts one parameter and return power of two. 
#Input : 4 Output : 16 
#Input : 6 Output : 64 

Square=lambda a:a**2

def main():
	print("Enter number")
	iValue=int(input())

	ret=Square(iValue)
	print(iValue,"to the power two is :",ret)

if __name__=="__main__":
	main()