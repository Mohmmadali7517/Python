
def main():
	i=0
	Arr=[]
	sum=0

	print("Enter the elements : ")
	for i in range(5):
		Arr.append(int(input()))

	print("Your entered elements are: ",Arr)

	for i in range(len(Arr)):
		sum=sum+Arr[i]
	print("Addition is: ",sum)
	
if __name__ == '__main__':
	main()