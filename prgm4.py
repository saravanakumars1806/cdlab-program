import string
exp = input("Enter an expression: ")
print("\nSymbol Table:")
print("Symbol\tAddress\t\tType")
for ch in exp:
    if ch in ['+', '-', '*', '/', '=']:
        print(f"{ch}\t{id(ch)}\tOperator")
    elif ch.isdigit():
        print(f"{ch}\t{id(ch)}\tDigit")
    elif ch.isalpha():
        print(f"{ch}\t{id(ch)}\tIdentifier")

