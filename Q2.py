#square root of aa number using function
def square_root(number):
    approx = number/2  # initial guess
    
    while True:
        new_approx = (approx + abs(number/approx)) / 2
        if abs(new_approx - approx) < 0.001:  # stopping condition
            return new_approx
        approx = new_approx

number = int(input("Enter number "))
result = square_root(number)
print(abs(result))