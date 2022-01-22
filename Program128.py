
def CheckDigit(c):
	if((c>='0')and(c<='9')):
		return True
	else:
		return False
		
def main():
	ch='\0'
	bRet=0

	print("Enter character")
	ch=str(input())

	bRet=CheckDigit(ch)
	if(bRet==True):
		print(ch,"is digit")
	else:
		print(ch,"is not digit")

if __name__=="__main__":
	main()