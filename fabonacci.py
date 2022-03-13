#to print the fabonacci series:0,1,1,2,3,5,8,13...
n=int(input("Enter a number:"))
a=0
b=1
s=0
count=1
while n>=0:
    a=b
    b=s
    s=a+b
    count+=1
print("The series",s)
input()
    
