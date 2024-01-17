"""
The program must be built using either C, C++, Java, or Python
The program must support the following operations: Logical Implication, Logical Inequality, Exclusive Disjunction, Logical NAND, and Logical NOR

Pseudo-code:
I will create a loop that tests for 2 valid True or False inputs.
A class will be created that contains methods for each logical test.
An output will be displayed using the class methods with the inputs.
"""

# Variables with userinput for test cases
# While loop tests for correct parameters
while True:
    try:
        boolx = int(input("Enter 1 (True) or 0 (False):"))
        # Input Validation to check for either 0 or 1
        if boolx not in {0,1}:
            continue
    # If the value isnt an int
    except ValueError:
        print("Incorrect Parameter Detected. Please enter 1 (True) or 0 (False):")
        continue
    else:
        break
while True:
    try:
        booly = int(input("Enter 1 (True) or 0 (False):"))
        # Input Validation to check for either 0 or 1
        if booly not in {0,1}:
            continue
    # If the value isnt an int
    except ValueError:
        print("Incorrect Parameter Detected. Please enter 1 (True) or 0 (False):")
        continue
    else:
        break

# Class Implementation
class Logic:
    def __init__(self, bool1, bool2):
        self.bool1 = bool1
        self.bool2 = bool2
    
    # Logical Implication
    def implication(self):
        if self.bool1 is self.bool2:
            print("True")
        elif self.bool1 == 1 and self.bool2 == 0:
            print("False")
        elif self.bool1 == 0 and self.bool2 == 1:
            print("True")
        elif self.bool1 == 0 and self.bool2 == 0:
            print("True")
        else:
            print("Incorrect Parameters entered")
    
    # Logic Equality
    def equality(self):
        if self.bool1 is self.bool2:
            print("True")
        elif self.bool1 is not self.bool2:
            print("False")
    
    # Exclusive Disjunction
    def disjunction(self):
        if self.bool1 is self.bool2:
            print("False")
        elif self.bool1 is not self.bool2:
            print("True")
    
    # Logical NAND
    def nand(self):
        if self.bool1 == 1 and self.bool2 == 1:
            print("False")
        else:
            print("True")
    
    # Logical NOR
    def nor(self):
        if self.bool1 == 0 and self.bool2 == 0:
            print("True")
        else:
            print("False")

# Class is called
logic = Logic(boolx, booly)

# Logical Implication
print("----------LOGICAL IMPLICATION----------")
logic.implication()

# Logical Equality
print("----------LOGICAL EQUALITY----------")
logic.equality()

# Exclusive Disjunction
print("----------EXCLUSIVE DISJUNCTION----------")
logic.disjunction()

# Logical NAND
print("----------LOGICAL NAND----------")
logic.nand()

# Logical NOR
print("----------LOGICAL NOR----------")
logic.nor()
    
print("----------PROGRAM END----------")
