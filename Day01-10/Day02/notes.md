## Sring Methods

name = input("Enter your name: ")

phone_number = input("Enter your phone #: ")

length = len(name)

index = name.find(" ")

name = name.capitalize()

name = name.upper()

name = name.lower()

result = name.isdigit()

result = name.isalpha()

result = phone_number.count(" ")

phone_number = phone_number.replace("-", "")

### indexing = accessing elements of a sequence using [] (indexing operator)

### [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[4:8])
print(credit_number[4:])
print(credit_number[-1])
print(credit_number[-4:])
print(credit_number[::2])
print(credit_number[::3])

# EXERCISE 2 -Reversing

credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1]
print(credit_number)

## Format Specifiers

format specifiers = {:flags} format a value based on what flags are inserted

.(number)f = round to that many decimal places

:(number) = allocate that many spaces

:0(number) = allocate and zero pad that many spaces

:< = left justify

:> = right justify

:^ = center align

:+ = use a plus sign to indicate positive value

:= = place sign to leftmost position

: = insert a space before positive numbers

:, = comma separator

:% = percentage format

### whileloop = perform some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
print("You did not enter your name!")
name = input("Enter your name: ")

print(f"Hello {name}")

## for loops = execute a block of code a fixed number of times.

You can iterate over a range, string, sequence, etc


for x in range(1, 11):
    print(x)


## nested loop = A loop within another loop (outer, inner)

outer loop:
    inner loop: