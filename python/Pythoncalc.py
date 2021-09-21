# Python Program 01 - Calculator (ENGR4)

#Written by Scoot Jones

#9.21.2021
   

sum_conastant = 1            #These constants make it easier and more readable
difference_constant = 2     #to pass the operation to the function 
product_constant = 3
quotient_constant = 4
modulo_constant = 5
def doMath(num1, num2, operation):
    if operation == sum_conastant:
        return num1 + num2
    if operation == difference_constant:
        return num1 - num2
    if operation == product_constant:
        return num1 * num2
    if operation == quotient_constant:
        return round(num1 / num2, 2)
    if operation == modulo_constant:
        return num1 % num2
        
print("scoots calculator")
a = int(input("Enter your first number: "))  #Sets each value to the number input by the user
b = int(input("Enter your second number: "))
        

print("Sum:\t\t" + str(doMath(a,b,sum_conastant)))               #Does each function for the input values
print("Difference:\t" + str(doMath(a,b,difference_constant)))
print("Product:\t" + str(doMath(a,b,product_constant)))
print("Quotient:\t" + str(doMath(a,b,quotient_constant)))
print("Modulo:\t\t" + str(doMath(a,b,modulo_constant)))
