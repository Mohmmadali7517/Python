#7. Write a program which accept one number and display below pattern. 
#Input : 5 
#Output : 
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5 
# 1 2 3 4 5

def DisplayPattern(iValue):

    for i in range(1,iValue+1):
        for j in range(1,iValue+1):
            print(j,"\t",end='')

        print()

def main():
    iValue=0

    print("Enter number ")
    iValue=int(input())

    DisplayPattern(iValue)

if __name__ == '__main__':
    main()