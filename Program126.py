
def CheckCapital(c):
	if(((ord(c))>=65)and((ord(c))<=90)):
		return True
	else:
		return False

def main():
	ch='\0'
	bRet=False

	print("Enter Character")
	ch=str(input())

	bRet=CheckCapital(ch)

	if(bRet==True):
		print(ch,"is capital letter")
	else:
		print(ch,"is not capital letter")

if __name__=="__main__":
	main()