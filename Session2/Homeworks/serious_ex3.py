#1
##a.
for i in range(20):
    print(i, end=" ")


n= int(input("enter a number? "))
for i in range(n):
    print(i, end= "")# 

##b.
for i in range(10):
    print("1", "0 ", end= "")

n= int(input("enter the total number of 1's and 0's"))
for i in range(n):
    print("1 ","0 ", end=" ")


##c.
n = int(input("enter a number? "))
for i in range(1, n, 1):
    for j in range(i , n* i, i):
        print(j, end=" ")
    print()


