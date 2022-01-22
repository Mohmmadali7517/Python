
def DisplayTable():
	i=0

	print("ASCII table is ")
	print("***************************")
	print("Decimal\tHexadecimal\tOctal\tCharacter\t")
	print("***************************")
	for i in range(128):
		print(i,"\t",hex(i),"\t",oct(i),"\t",chr(i))
		
def main():
	DisplayTable()

if __name__=="__main__":
	main()