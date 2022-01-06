#6. Write a program which accept one number and display below pattern. 
#Input : 5 
#Output : 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def DisplayPattern(iNo):
    for i in range(iNo,0,-1):
        for j in range(1,iNo+1):
            if(i>=j):
                print("*\t",end='')
            else:
                print("\t",end='')
        print()        

def main():
    iValue=0

    print("Enter number")
    iValue=int(input())

    DisplayPattern(iValue)

if __name__=="__main__":
    main()