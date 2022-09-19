#Write a program that takes a number and determine whether it is a tens, hundred, thousand 
#or million. Use arithmetic operation to determine this.
def determine(num):
    if len(str(num//10)) == 1 and num > 9:
        return "the number input is tens"
    elif len(str(num//10)) == 2:
        return "the number input is hundred"
    elif len(str(num//10)) in range (3, 6) :
        return "the number input is thousand"
    elif len(str(num//10)) == 6:
        return "the number input is million"    
print(determine(200))