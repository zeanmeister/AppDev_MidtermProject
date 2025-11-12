
# 1. RENAME (Shift + F6)
def greet_user(name):
    print("Hello,", name)

# Try renaming greet_user → say_hello
greet_user("Ken")


# 2. EXTRACT VARIABLE / CONSTANT (Ctrl + Alt + V / Ctrl + Alt + C)
def compute_total(price, quantity):
    total = (price * quantity) + (price * quantity * 0.12)  # 12% tax
    print(total)

print("Total:", compute_total(100, 2))


# 3. REFORMAT CODE (Ctrl + Alt + L)
# Intentionally messy function:
def calc(x,y):return x+y
print("Sum:",calc(10,5))
# Try reformatting this function using Code Cleanup


# 4. CHANGE SIGNATURE (Ctrl + F6)
def display_info(name):
    print("Name:", name)

# Try adding a new parameter "age" and update function calls automatically
display_info("Miguel")


# 5. MOVE / REFACTOR DIRECTORY (F6)
# Move this helper function to another file (e.g., refactoring_demo2.py)
def convert_to_uppercase(word):
    return word.upper()

print(convert_to_uppercase("python"))


# 6. SAFE DELETE (Alt + Delete)
def unused_function():
    print("This function is not used anywhere!")

# Try using Safe Delete to remove "unused_function"
