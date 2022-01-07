"""5.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will 
return Maximum number from that numbers. (You can also use normal functions instead of 
lambda functions). 
Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
List after filter = [2, 11, 17, 23, 31] 
List after map = [4, 22, 34, 46, 62] 
Output of reduce = 62
"""
import Module as M 
from functools import reduce

Prime=lambda no : M.Prime(no)

Mult=lambda no:no*2

Maximum=lambda no1,no2:M.Maximum(no1,no2)

def main():
	Data=[]
	print("Enter number of elements in list ")
	iSize=int(input())

	print("Enter numbers in list")
	for i in range(iSize):
		Data.append(int(input()))

	print("elements in list are :",Data)

	newdata=list(filter(Prime,Data))
	print("Data after filter :",newdata)

	Increment=list(map(Mult,newdata))
	print("Data after map :",Increment)

	ret=reduce(Maximum,Increment)
	print("Maximum number is :",ret)

if __name__=="__main__":
	main()