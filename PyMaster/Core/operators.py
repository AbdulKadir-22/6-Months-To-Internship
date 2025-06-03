"""
operators.py

A comprehensive guide to Python operators with examples.
Covers:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators
"""

def arithmetic_operators():
    print("\n🔢 Arithmetic Operators")
    a, b = 10, 3
    print(f"{a} + {b} = {a + b}")      # Addition
    print(f"{a} - {b} = {a - b}")      # Subtraction
    print(f"{a} * {b} = {a * b}")      # Multiplication
    print(f"{a} / {b} = {a / b:.2f}")  # Division
    print(f"{a} % {b} = {a % b}")      # Modulus
    print(f"{a} ** {b} = {a ** b}")    # Exponentiation
    print(f"{a} // {b} = {a // b}")    # Floor Division

def assignment_operators():
    print("\n📝 Assignment Operators")
    x = 5
    print(f"Initial x = {x}")
    x += 3; print(f"x += 3 → {x}")
    x -= 2; print(f"x -= 2 → {x}")
    x *= 4; print(f"x *= 4 → {x}")
    x /= 2; print(f"x /= 2 → {x}")
    x %= 3; print(f"x %= 3 → {x}")
    x **= 2; print(f"x **= 2 → {x}")
    x //= 2; print(f"x //= 2 → {x}")

def comparison_operators():
    print("\n📊 Comparison Operators")
    a, b = 7, 5
    print(f"{a} == {b} → {a == b}")
    print(f"{a} != {b} → {a != b}")
    print(f"{a} > {b} → {a > b}")
    print(f"{a} < {b} → {a < b}")
    print(f"{a} >= {b} → {a >= b}")
    print(f"{a} <= {b} → {a <= b}")

def logical_operators():
    print("\n🧠 Logical Operators")
    a, b = True, False
    print(f"{a} and {b} → {a and b}")
    print(f"{a} or {b} → {a or b}")
    print(f"not {a} → {not a}")

def bitwise_operators():
    print("\n🧮 Bitwise Operators")
    a, b = 10, 4  # Binary: 1010 & 0100
    print(f"{a} & {b} = {a & b}  # AND")
    print(f"{a} | {b} = {a | b}  # OR")
    print(f"{a} ^ {b} = {a ^ b}  # XOR")
    print(f"~{a} = {~a}          # NOT")
    print(f"{a} << 1 = {a << 1}  # Left shift")
    print(f"{a} >> 1 = {a >> 1}  # Right shift")

def membership_operators():
    print("\n🧾 Membership Operators")
    fruits = ['apple', 'banana', 'cherry']
    print("'banana' in fruits →", 'banana' in fruits)
    print("'grape' not in fruits →", 'grape' not in fruits)

def identity_operators():
    print("\n🪞 Identity Operators")
    x = [1, 2]
    y = x
    z = [1, 2]
    print(f"x is y → {x is y}")     # True, same object
    print(f"x is z → {x is z}")     # False, different objects
    print(f"x == z → {x == z}")     # True, same contents
    print(f"x is not z → {x is not z}")

def demo():
    print("\n=== 💡 Demo: Python Operators ===")
    arithmetic_operators()
    assignment_operators()
    comparison_operators()
    logical_operators()
    bitwise_operators()
    membership_operators()
    identity_operators()
    print("\n=== 🔚 End of Operators Module ===")

# Run the demo when this file is executed directly
if __name__ == "__main__":
    demo()
