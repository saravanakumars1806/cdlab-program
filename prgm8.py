grammar = {
    'S': ['AB'],
    'A': ['a'],
    'B': ['b']
}
follow = {
    'S': {'$'},
    'A': set(),
    'B': set()
}
follow['A'].add('b')
print("FOLLOW(S) =", follow['S'])
print("FOLLOW(A) =", follow['A'])
print("FOLLOW(B) =", follow['B'])
