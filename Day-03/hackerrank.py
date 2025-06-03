# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i .
# print: Print the list.
# remove e: Delete the first occurrence of integer e .
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by  lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Initialize the list
my_list = []

# Read the number of commands
n = int(input())

# Iterate through each command
for _ in range(n):
    command = input().strip().split()
    cmd = command[0]

    if cmd == "insert":
        i = int(command[1])
        e = int(command[2])
        my_list.insert(i, e)
    elif cmd == "print":
        print(my_list)
    elif cmd == "remove":
        e = int(command[1])
        if e in my_list:
            my_list.remove(e)
    elif cmd == "append":
        e = int(command[1])
        my_list.append(e)
    elif cmd == "sort":
        my_list.sort()
    elif cmd == "pop":
        if my_list:
            my_list.pop()
    elif cmd == "reverse":
        my_list.reverse()
