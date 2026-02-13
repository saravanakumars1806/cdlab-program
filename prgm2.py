exp = input("Enter expression: ")
for ch in exp:
    if ch.isalpha():
        print("Identifier:", ch)
    elif ch.isdigit():
        print("Number:", ch)
    elif ch in "+-*/=%<>!":
        print("Operator:", ch)
    elif ch in "(){}[];,:":        
        print("Punctuator:", ch)
    elif not ch.isspace():
        print("Special Character:", ch)
