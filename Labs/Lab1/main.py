"""
The program must be built using either C, C++, Java, or Python
The program must support the following operations: Logical Implication, Logical Inequality, Exclusive Disjunction, Logical NAND, and Logical NOR
"""
# Variables with userinput for test cases
# While loop tests for correct parameters
while True:
    try:
        bool1 = int(input("Enter 1 (True) or 0 (False):"))
        if bool1 not in {0,1}:
            continue
    except ValueError:
        print("Incorrect Parameter Detected. Please enter 1 (True) or 0 (False):")
        continue
    else:
        break
while True:
    try:
        bool2 = int(input("Enter 1(True) or 0(False):"))
        if bool2 not in {0,1}:
            continue
    except ValueError:
        print("Incorrect Parameter Detected. Please enter 1 (True) or 0 (False):")
        continue
    else:
        break

# Logical Implication
print("----------LOGICAL IMPLICATION----------")
if bool1 is bool2:
    print("True")
elif bool1 == 1 and bool2 == 0:
    print("False")
elif bool1 == 0 and bool2 == 1:
    print("True")
elif bool1 == 0 and bool2 == 0:
    print("True")
else:
    print("Incorrect Parameters entered")

# Logical Equality
print("----------LOGICAL EQUALITY----------")
if bool1 is bool2:
    print("True")
elif bool1 is not bool2:
    print("False")
else:
    print("Incorrect Parameters entered")

# Exclusive Disjunction
print("----------EXCLUSIVE DISJUNCTION----------")
if bool1 == 0 and bool2 == 0:
    print("False")
elif bool1 == 1 and bool2 == 0:
    print("True")
elif bool1 == 0 and bool2 == 1:
    print("True")
elif bool1 == 1 and bool2 == 1:
    print("False")
else:
    print("Incorrect parameters entered")

# Logical NAND
print("----------LOGICAL NAND----------")
if bool1 == 0 and bool2 == 0:
    print("False")
elif bool1 == 1 and bool2 == 0:
    print("True")
elif bool1 == 0 and bool2 == 1:
    print("True")
elif bool1 == 1 and bool2 == 1:
    print("False")
else:
    print("Incorrect parameters entered")

# Logical NOR
print("----------LOGICAL NOR----------")
if bool1 == 0 and bool2 == 0:
    print("True")
elif bool1 == 1 and bool2 == 0:
    print("False")
elif bool1 == 0 and bool2 == 1:
    print("False")
elif bool1 == 1 and bool2 == 1:
    print("False")
else:
    print("Incorrect parameters entered")
    
print("----------PROGRAM END----------")
