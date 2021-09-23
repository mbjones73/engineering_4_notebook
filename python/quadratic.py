from math import sqrt
def findDiscriminant(a, b, c): 
    discriminant = b ** 2 -4*a*c
    return discriminant
def findRoots(a, b, c):
    root1 = round((-1*b - sqrt(b**2 - 4*a*c)) / (2*a), 3) 
    root2 = round((-1*b + sqrt(b**2 - 4*a*c)) / (2*a), 3)
    return [root1, root2]


userInput = ""

print("Scoots Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + x = 0")
while userInput != "x":
    a = int(input("Enter coefficient a: ")) 
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))
    if  findDiscriminant(a, b, c) < 0: 
        print("There are no real roots") #this tells if you have no real roots
        
    else:
        print("Root #1: " + str(findRoots(a, b, c)[0])) # Prints the first root
        print("Root #2: " + str(findRoots(a, b, c)[1])) # Prints the second root
    userInput = input("Press Enter to run again, press x then Enter to exit: ") # Asks for input to run again or quit
print("Program exited") 
