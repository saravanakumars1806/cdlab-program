import keyword
print("Keywords of python:")
print(keyword.kwlist)
print("Enter your program (press Enter on empty line to finish):")
code = ""
while True:
    line = input()
    if line.strip() == "":
        break
    code += " " + line
tokens = code.replace("(", " ").replace(")", " ").replace('"', " ") \
             .replace(",", " ").replace(":", " ").split()
found = set()
for t in tokens:
    if keyword.iskeyword(t):
        found.add(t)
print("Keywords present:", found)


