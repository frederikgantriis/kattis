values = input().split()

p = int(values[0])
n = int(values[1])
lastReplace = 0

parts = []

for i in range(n):
    newPart = input()
    if newPart not in parts:
        parts.append(newPart)
        lastReplace = i+1
    
if len(parts) != p:
    print("paradox avoided")
else:
    print(lastReplace)
    