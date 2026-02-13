text = """Hello world
This is Python
Welcome!!!!"""
a = text.split()
words_count = len(a)
space_count = text.count(" ")
newline_count = text.count("\n")
count = count1 = special_count = 0
for i in text:
    if i.isdigit():
        count = count + 1
    elif i.isalpha():
        count1 = count1 + 1
    elif not i.isspace():
        special_count = special_count + 1
print("Number of whitespaces:", space_count)
print("Number of newline characters:", newline_count)
print("Number of words:", words_count)
print("Number of digits:", count)
print("Number of alphabets:", count1)
print("Number of special characters:", special_count)
