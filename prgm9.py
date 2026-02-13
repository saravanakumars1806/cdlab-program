stack = []
input_string = "id+id$"
print("Stack\tInput\tAction")
stack.append('i')
print(stack, input_string[1:], "Shift")
stack.append('d')
print(stack, input_string[2:], "Shift")
stack.clear()
stack.append('E')
print(stack, "+id$", "Reduce E -> id")
stack.append('+')
print(stack, "id$", "Shift")
stack.append('i')
print(stack, "d$", "Shift")
stack.append('d')
print(stack, "$", "Shift")
stack = ['E', '+', 'E']
print(stack, "$", "Reduce E -> id")
stack = ['E']
print(stack, "$", "Reduce E+E -> E")
print(stack, "$", "Accept")



