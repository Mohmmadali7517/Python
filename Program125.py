def CheckCapital(c):
	if((c>='A')and(c<='Z')):
		return True
	else:
		return False

def main():
	ch=0
	bret=False

	print("Enter character")
	ch=str(input())

	bret=CheckCapital(ch)
	if(bret==True):
		print(ch,"is capital letter")
	else:
		print(ch,"is not capital letter")

if __name__=="__main__":
	main()
