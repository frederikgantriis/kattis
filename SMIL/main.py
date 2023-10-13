arr = input()

indexs = []

for i in range(len(arr)):
    if i != len(arr)-1 and arr[i] == ":" or arr[i] == ";":
        if arr[i+1] == ")":
            indexs.append(i)
        elif i+2 != len(arr) and arr[i+1] == "-":
            if arr[i+2] == ")":
                indexs.append(i)

for i in range(len(indexs)):
    print(indexs[i])