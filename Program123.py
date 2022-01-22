
def DisplayTable():
	i=0

	print("ASCII table is")
	print("******************************************")
	print("Decimal\t",end=''+"Character\n")
	print("******************************************")
	for i in range(128):
		print(i,"\t"+chr(i))
	print("******************************************")

def main():
	DisplayTable()

if __name__=="__main__":
	main()