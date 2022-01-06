#2. Write a program which accept one number and display below pattern.
#Input : 5
#Output : 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * * 

def Display(iNo):
    for i in range(iNo):
        for i in range(iNo):
            print("*\t",end='')

        print()

def main():
    iValue=0

    print("Enter Number")
    iValue=int(input())

    Display(iValue)

if __name__ == '__main__':
    main()