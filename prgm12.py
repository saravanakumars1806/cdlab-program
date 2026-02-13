

def remove_dead_code(code):
    used = ""
    optimized = []
    return_found = False


    for line in code:
        if "=" not in line:
            used += line

    for line in code:
        if return_found:
            continue  

        if "return" in line:
            return_found = True
            optimized.append(line)
            continue

        if "=" in line:
            var = line.split("=")[0].strip()
            if var in used:
                optimized.append(line)
            else:
                print("Removed:", line)
        else:
            optimized.append(line)

    return optimized


code = [
    "a = 10",
    "b = 20",
    "c = a + 5",
    "d = 50",
    "return c",
    "e = 100"
]

result = remove_dead_code(code)

print("\nOptimized Code:")
for line in result:
    print(line)
