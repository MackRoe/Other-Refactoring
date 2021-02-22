# by Kami Bigdely 
# Replace magic numbers with named constanst
ELECTRIC_FORCE_CONSTANT = .9875517923*1e9


# First Section
# Given two point charges, calcualte the electric force exerted on them.
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance be10tween two charges: "))
force = ELECTRIC_FORCE_CONSTANT * q1 * q2/(distance**2)
print ("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
num = int(input('Enter an integer number: '))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")