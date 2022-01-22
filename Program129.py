
def SmallToCapital(c):
	if((c>='a')and(c<='z')):
		return chr(ord(c)-32)

def main():
	ch='\0'
	cRet='0'

	print("Enter Character")
	ch=str(input())

	cRet=SmallToCapital(ch)

	print("Capital letter is :",cRet)

if __name__=="__main__":
	main()