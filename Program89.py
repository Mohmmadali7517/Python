
def DisplayPattern(iRows,iCols):
	for i in range(1,iRows+1):
		for j in range(1,iCols+1):
			print(i,"\t",end='')
		print()
def main():
	iValue1,iValue2=0,0

	print("Enter the number of rows")
	iValue1=int(input())

	print("Enter the number of Cols")
	iValue2=int(input())

	DisplayPattern(iValue1,iValue2)

if __name__ == '__main__':
	main()