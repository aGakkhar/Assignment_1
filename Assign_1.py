#### SWAP TWO NUMBERS ####


a = input("Enter Number a   ")
b = input("Enter Number b   ")

a1 = a
b1 = b 


print("Swapped Numbers are a = ", b1)
print("Swapped Numbers are b = ", a1)

#### CALCULATE FACTORIAL ####

f = int(input("Enter the number to calculate its factorial  "))
fact = 1
while f >= 1:
    fact = fact * f
    f = f-1
    if f == 0:
        break

print ("Factorial is ", fact)
    

#### CALCULATE FIBONACCI SERIES ####

x = int(input("Enter the number of elemetns in the series "))

f = [0,1]

for i in range(0,x):
    t = f[(len(f) - 1)] + f[(len(f) - 2)]
    f.append(t)

print ("Fibonacci Series \n",f)

#### STRING OPERATIONS ####

string1 = input("Enter sample string 1 ")
string2 = input("Enter sample string 2 ")


print ("Length of string 1 ", len(string1))
print ("Length of string 2 ", len(string2))

string3 = string1 + string2

print ("Concatenated String ", string3)

print ("First 3 letters in the string (Substring)", string3[0:3] )


#### CALCULATOR ####

a = float(input("Enter First Number "))
b = float(input("Enter Second Number "))

sum = a+b
sub = a-b
mul = a*b
div = a/b

print ("The Sum is ", sum)
print ("The Difference is ", sub)
print ("The Mutiplication is ", mul)
print ("The Division is ", div)