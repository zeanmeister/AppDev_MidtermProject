# ======================================================
# PyCharm Refactoring Demo Script
# Demonstration of: Rename → Extract Variable → Reformat →
# Extract Method → Change Signature → Inline → Move → Safe Delete
# ======================================================

# 1. RENAME (Shift + F6)
def greet_user(name):
    print("Hello,", name)

# Try renaming greet_user → say_hello
greet_user("Ken")


# 2. EXTRACT VARIABLE / CONSTANT (Ctrl + Alt + V / Ctrl + Alt + C)
def compute_total(price, quantity):
    total = (price * quantity) + (price * quantity * 0.12)  # 12% tax
    return total

# Try extracting "price * quantity * 0.12" as a variable "tax"
# Or extract 0.12 as constant TAX_RATE
print("Total:", compute_total(100, 2))


# 3. REFORMAT CODE (Ctrl + Alt + L)
# Intentionally messy function:
def calc(x,y):return x+y
print("Sum:",calc(10,5))
# Try reformatting this function using Code Cleanup


# 4. EXTRACT METHOD / FUNCTION (Ctrl + Alt + M)
def process_data(data):
    cleaned = [x.strip().lower() for x in data]
    cleaned.sort()
    print("Processed data:", cleaned)

# Try extracting the cleaning part into a new function "clean_data"
data_list = [" Apple ", "banana ", " Cherry"]
process_data(data_list)


# 5. CHANGE SIGNATURE (Ctrl + F6)
def display_info(name):
    print("Name:", name)

# Try adding a new parameter "age" and update function calls automatically
display_info("Miguel")


# 6. INLINE (Ctrl + Alt + N)
def calc_discount(price):
    discount = price * 0.10
    return discount

# Try inlining variable "discount"
print("Discount:", calc_discount(1000))


# 7. MOVE / REFACTOR DIRECTORY (F6)
# Move this helper function to another file (e.g., utils.py)
def convert_to_uppercase(word):
    return word.upper()

print(convert_to_uppercase("python"))


# 8. SAFE DELETE (Alt + Delete)
def unused_function():
    print("This function is not used anywhere!")

# Try using Safe Delete to remove "unused_function"
