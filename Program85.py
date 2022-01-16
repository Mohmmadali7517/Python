
def Display(iNo):
	ch='a'
	for i in range(1,iNo+1):
		print(ch,"\t",end='')
		ch=chr(ord(ch)+1)

def main():
	iValue=0

	print("Enter number ")
	iValue=int(input())

	Display(iValue)

if __name__ == '__main__':
	main()