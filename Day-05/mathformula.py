
def addition(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

def circumference(radius):
    total = 2 * 3.14159263 * radius
    return total