#3.Write a program which contains filter(), map() and reduce() in it. Python application which 
#contains one list of numbers. List contains the numbers which are accepted from user. Filter 
#should filter out all such numbers which greater than or equal to 70 and less than or equal to 
#90. Map function will increase each number by 10. Reduce will return product of all that numbers. 

from functools import reduce

Range=lambda no:(no>=70 and no<=90)

Increment=lambda no : no+10

Mult=lambda a,b:a*b

def main():

	Data=[]
	print("Enter how many elements you want")
	iSize=int(input())

	print("Enter number in list")
	for i in range(iSize):
		Data.append(int(input()))
	print("Original data :",Data)

	newdata=list(filter(Range,Data))
	print("Data after filter :",newdata)

	IncrementData=list(map(Increment,newdata))
	print("Data after map : ",IncrementData)

	ret=reduce(Mult,IncrementData)
	print("Data after reduce : ",ret)

if __name__=="__main__":
	main()