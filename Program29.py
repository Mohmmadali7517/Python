"""4.Write a program which contains filter(), map() and reduce() in it. Python application which 
contains one list of numbers. List contains the numbers which are accepted from user. Filter 
should filter out all such numbers which are even. Map function will calculate its square. 
Reduce will return addition of all that numbers. 
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
List after filter = [2, 4, 4, 2, 8, 10] 
List after map = [4, 16, 16, 4, 64, 100] 
Output of reduce = 204
"""

from functools import reduce

Even=lambda no : (no%2 ==0)

square=lambda no : (no**2)

Addition=lambda no1,no2 : no1+no2

def main():
	Data=[]
	print("Enter number of elements in list")
	iSize=int(input())

	print("Enter number in list")
	for i in range(iSize):
		Data.append(int(input()))
	print("Elements in list are :",Data)

	newdata=list(filter(Even,Data))
	print("Data after filter :",newdata)

	mapdata=list(map(square,newdata))
	print("Data after map : ",mapdata)

	ret=reduce(Addition,mapdata)
	print("Data after Addition : ",ret)

if __name__=="__main__":
	main()