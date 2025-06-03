
# data_types_and_typecasting.py

# 📘 DATA TYPES:
# In Python, every value has a data type. These types define what operations the value can perform.

# Main built-in data types:
# - int
# - float
# - str
# - bool
# - list: A list is an ordered, mutable collection that can contain elements of mixed data types,
#         including duplicates.
# - tuple: A tuple is an ordered, immutable collection that can contain elements of mixed data types, 
#          including duplicates.
# - dict:  A dictionary is an unordered, mutable collection of key-value pairs.
# - set: A set is an unordered, mutable collection of unique elements (no duplicates allowed).
# - NoneType

# 📘 TYPE CASTING:
# Type casting means converting one data type to another.
# - Implicit: Done automatically by Python
# - Explicit: Done manually by the programmer using functions like int(), float(), str(), etc.



def basic_data_types():
    print("\n📚 Basic Data Types in Python")
    
    integer_value = 42
    float_value = 3.14
    string_value = "Hello, Python!"
    boolean_value = True
    list_value = [1, 2, 3]
    tuple_value = (4, 5, 6)
    dict_value = {"name": "Yusu", "age": 18}
    set_value = {1, 2, 3}
    none_value = None

    print(f"int → {integer_value} ({type(integer_value).__name__})")
    print(f"float → {float_value} ({type(float_value).__name__})")
    print(f"str → {string_value} ({type(string_value).__name__})")
    print(f"bool → {boolean_value} ({type(boolean_value).__name__})")
    print(f"list → {list_value} ({type(list_value).__name__})")
    print(f"tuple → {tuple_value} ({type(tuple_value).__name__})")
    print(f"dict → {dict_value} ({type(dict_value).__name__})")
    print(f"set → {set_value} ({type(set_value).__name__})")
    print(f"NoneType → {none_value} ({type(none_value).__name__})")

def implicit_type_casting():
    print("\n🔁 Implicit Type Casting")
    a = 5        # int
    b = 2.0      # float
    c = a + b    # result will be float
    print(f"{a} (int) + {b} (float) = {c} ({type(c).__name__})")

def explicit_type_casting():
    print("\n✍️ Explicit Type Casting")
    x = "100"
    y = int(x)        # string to int
    z = float(x)      # string to float
    w = str(3.14)     # float to string

    print(f"int('{x}') = {y} ({type(y).__name__})")
    print(f"float('{x}') = {z} ({type(z).__name__})")
    print(f"str(3.14) = '{w}' ({type(w).__name__})")

    print("\n⚠️ Invalid Cast Example:")
    try:
        bad = int("Hello")  # This will fail
    except ValueError as e:
        print(f"int('Hello') → Error: {e}")

def casting_between_collections():
    print("\n🔄 Casting Between Collections")
    my_list = [1, 2, 3]
    my_tuple = tuple(my_list)
    my_set = set(my_list)

    print(f"List to Tuple: {my_tuple}")
    print(f"List to Set: {my_set}")

    my_str = "123"
    my_int = int(my_str)
    print(f"String '123' to int: {my_int}")

def demo():
    print("\n=== 🧪 Demo: Data Types & Type Casting ===")
    basic_data_types()
    implicit_type_casting()
    explicit_type_casting()
    casting_between_collections()
    print("\n=== 🔚 End of Data Types & Type Casting ===")

if __name__ == "__main__":
    demo()
