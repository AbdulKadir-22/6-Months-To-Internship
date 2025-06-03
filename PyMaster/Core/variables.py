"""
variables.py

📘 Definition:
A variable is a name that refers to a value stored in memory. In Python, variables are created when you assign them a value — no explicit declaration needed.

💡 Python is dynamically typed: the type of variable is determined at runtime.
"""

def declaration_and_assignment():
    print("\n📌 Declaration and Assignment")
    # Creating variables of various types
    name = "Yusu"
    age = 18
    height = 5.9
    is_student = True

    print(f"name = {name} (type: {type(name).__name__})")
    print(f"age = {age} (type: {type(age).__name__})")
    print(f"height = {height} (type: {type(height).__name__})")
    print(f"is_student = {is_student} (type: {type(is_student).__name__})")

def naming_rules():
    print("\n📏 Naming Rules and Conventions")
    _valid_name = "underscore is fine"
    camelCase = "less common in Python"
    snake_case = "preferred_style"
    UPPER_CASE = "used for constants"

    print(f"_valid_name: {_valid_name}")
    print(f"camelCase: {camelCase}")
    print(f"snake_case: {snake_case}")
    print(f"UPPER_CASE (constant): {UPPER_CASE}")

def dynamic_typing():
    print("\n🧬 Dynamic Typing")
    x = 42
    print(f"x = {x} (type: {type(x).__name__})")

    x = "Now I'm a string"
    print(f"x = {x} (type: {type(x).__name__})")

    x = [1, 2, 3]
    print(f"x = {x} (type: {type(x).__name__})")

def multiple_assignment():
    print("\n🎯 Multiple Assignment")
    a, b, c = 1, 2, 3
    print(f"a = {a}, b = {b}, c = {c}")

    x = y = z = "Same value"
    print(f"x = {x}, y = {y}, z = {z}")

def variable_swapping():
    print("\n🔄 Variable Swapping")
    a, b = 10, 20
    print(f"Before Swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After Swap:  a = {a}, b = {b}")

def constants_demo():
    print("\n🔒 Constants (By Convention)")
    PI = 3.14159
    GRAVITY = 9.8
    print(f"PI = {PI}, GRAVITY = {GRAVITY}")
    print("Note: Python doesn't enforce constants — use ALL_CAPS to signal 'Do Not Change'.")

def type_checking():
    print("\n🔍 Type Checking")
    val = 99
    print(f"{val} is of type {type(val).__name__}")

    val = "Python"
    print(f"{val} is of type {type(val).__name__}")

def demo():
    print("\n=== 🧪 Demo: Variables in Python ===")
    declaration_and_assignment()
    naming_rules()
    dynamic_typing()
    multiple_assignment()
    variable_swapping()
    constants_demo()
    type_checking()
    print("\n=== 🔚 End of Variables Module ===")

# Run the demo when the file is executed directly
if __name__ == "__main__":
    demo()
