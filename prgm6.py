parsing_table = {
    ('E', 'id'): "E -> T E'",
    ("E'", '+'): "E' -> + T E'",
    ("E'", '$'): "E' -> ε",
    ('T', 'id'): "T -> id"
}
non_terminals = ['E', "E'", 'T']
terminals = ['id', '+', '$']
print("Predictive Parsing Table:\n")
print(f"{'NT/T':<8}", end="")
for t in terminals:
    print(f"{t:<10}", end="")
print()
for nt in non_terminals:
    print(f"{nt:<8}", end="")
    for t in terminals:
        rule = parsing_table.get((nt, t), "")
        print(f"{rule:<10}", end="")
    print()
