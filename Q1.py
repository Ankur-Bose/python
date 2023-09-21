#factorial using recursive as well as non recursive
def fact(x):
    pro = 1
    for i in range (1,x+1):
        pro*=i
    return pro

def factrec(x):
    pro=1
    if(x==1):
        return 1
    else:
        return x*factrec(x-1)

x=int(input("Enter number \n"))
print(factrec(x))