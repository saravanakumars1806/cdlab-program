grammar = {
    'S': ['aA'],
    'A': ['bB'],
    'B': ['cC'],
    'C': ['d']
}

first = {}

def FIRST(x):
    if x not in grammar:
        return {x}
    if x in first:
        return first[x]
    
    first[x] = set()
    for p in grammar[x]:
        first[x].add(p[0])
    
    return first[x]

for nt in grammar:
    print("FIRST(", nt, ") =", FIRST(nt))

print("FIRST:", first)
