#first one
def gojo(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n")

#second one
def naruto(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("*",end=" ")
        print("\n")

#third
def sukuna(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\n")

#fourth
def zoro(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("\n")

#fifth
def lucifer(n):
    num = 1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num = num+1
        print("\n")