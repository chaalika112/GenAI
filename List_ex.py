name = ["chaalika","pavan",1,2,3,["Raji","Aditya"]]

for x in name:
    print(x)

print(name[3])

print(name[5][1])

print(len(name))

print(name[-1])

# in built functions of a list 

a = [2,6,8,5]

print(min(a))
print(max(a))
print(sum(a))
print(sorted(a))

# keyword - append / clear / copy

name = ["pavan", "Raji", "Dedeepya", "Aditya" ]

name.append("King")

name.clear()
print(name)

name2 = name.copy()
print(name2)

print(name.count("Raji"))



