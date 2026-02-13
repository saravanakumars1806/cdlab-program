exp = input("Enter an expression: ")
for ch in exp:
    if ch.isalpha():
        print("Identifier:", ch)
    elif ch.isdigit():
        print("Number:", ch)
    elif ch in "+-*/=":
        print("Operator:", ch)
    elif ch in "(){}[];,":
        print("Punctuator:", ch)
    elif ch.isspace():
        pass
    else:
        print("Special:", ch)
