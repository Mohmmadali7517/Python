def ToggleChar(c):
	if((c>='A')and(c<='Z')):
		return chr(ord(c)+32)
	elif((c>='a')and(c<='z')):
		return chr(ord(c)-32)

def main():
	ch='\0'
	cRet='\0'

	print("Enter character")
	ch=str(input())

	cRet=ToggleChar(ch)
	print("Toggle character is :",cRet)


if __name__=="__main__":
	main()