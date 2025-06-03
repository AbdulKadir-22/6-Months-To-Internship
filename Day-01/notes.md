- Variables and Data types
    
    ### Varibales
    
    **Variable = A container for a value (string, integer, float, boolean)**
    
    **A variable behaves as if it was the value it contains**
    
    **Strings**
    
    first_name = "Bro"
    food = "pizza"
    email = "Bro123@fake.com"
    
    **Integers**
    
    age = 25
    quantity = 3
    num_of_students = 30
    
    **Float**
    
    price = 10.99
    gpa = 3.2
    distance = 5.5
    
    **Boolean**
    
    is_student = True
    for_sale = False
    is_online = True
    
    ### Typecasting
    
    **type casting = The process of converting a value of one data type to another**
    
    **(string, integer, float, boolean)**
    
    **Explicit vs Implicit**
    
    name = "Bro"
    age = 21
    gpa = 1.9
    student = True
    
    **print(type(name))**
    
    **print(type(age))**
    
    **print(type(gpa))**
    
    **print(type(student))**
    
    age = float(age)
    print(age)
    
    gpa = int(gpa)
    print(gpa)
    
    student = str(student)
    print(student)
    
    name = bool(name)
    print(name)
    
    ### User Input
    
    User input without type casting is always a string 
    
    ```python
    Name = input(”Enter you name: ”)
    ```
    
- Math and Operators
    
    ### Built in Math  Functions
    
    ```python
    x = 5.5
    round(x)
    abs(x)
    pow(x,2)
    max(x,y,z)
    min(x,y,z)
    ```
    
    ### Math Library
    
    ```python
    import math
    math.pi
    math.e
    math.sqrt
    math.floor
    
    ```
    
- Conditional
    
    ### if = Do some code IF condition is True
    
    ### else = Do something else if above condition/s are False