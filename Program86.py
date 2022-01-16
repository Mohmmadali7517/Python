
def Display():
	iRow=3
	iCol=4

	for i in range(1,iRow+1):
		for j in range(1,iCol+1):
			print("*\t",end='')
		print()

def main():
	Display()

if __name__=="__main__":
	main()