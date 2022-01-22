def CapitalToSmall(c):
	if((c>='A')and(c<='Z')):
		return chr(ord(c)+32)

def main():
	ch='\0'
	cret='\0'

	print("Enter Capital Character")
	ch=str(input())

	cret=CapitalToSmall(ch)
	print("Small letter is :",cret)

if __name__=="__main__":
	main()