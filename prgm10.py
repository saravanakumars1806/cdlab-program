expr = "a=b*c+d/e-f"
temp = 1
print("Three Address Code:")
print("t"+str(temp), "= b * c")
temp += 1
print("t"+str(temp), "= d / e")
temp += 1
print("t"+str(temp), "= t1 + t2")
temp += 1
print("t"+str(temp), "= t3 - f")
temp += 1
print("a = t4")
