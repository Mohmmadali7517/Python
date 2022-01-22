
def ChackSmall(c):
	if((c>='a')and(c<='z')):
		return True
	else:
		return False

def main():
	ch='\0'
	bret=False

	print("Enter character")
	ch=str(input())

	bret=ChackSmall(ch)
	if(bret==True):
		print(ch,"is small character")
	else:
		print(ch,"is not small character")

if __name__=="__main__":
	main()