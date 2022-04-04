class Calculator:
    #adds the two values taken in and print it out
    def adder(a , b):
        add = a + b
        print(add)
    #subtract the two values taken in and print it out
    def subtractor(a , b):
        sub = a - b
        print(sub)
    #multiply the two values taken in and print it out
    def multiplier(a , b):
        mul = a * b
        print(mul)
    #divide the two values taken in and print it out
    def divider(a , b):
        div = a / b
        print(div)
    #reset calculator to 0
    def clear():
        print(0)


calc = Calculator
#get user input values
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
#peform the various operations in the Calculator class
calc.adder(x,y)
calc.subtractor(x,y)
calc.multiplier(x,y)
calc.divider(x,y)
calc.clear()
