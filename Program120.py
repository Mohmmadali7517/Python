def Display(Brr):
	i=0
	while(i!=len(Brr)):
		print(Brr[i])
		i+=1

def main():
	Arr=0

	print("Enter your name")
	Arr=str(input())

	Display(Arr)

if __name__=="__main__":
	main()