import sys

counter = 0

while True:
    line = input()

    counter += 1

    toNext = False
    first = True
    second = True

    whitePixels, blackPixels, prevspace, space = 0, 0, 0, 0

    if line == "END":
        sys.exit()

    for i in line:
        

        if i == "*":
            blackPixels += 1


            if prevspace == 0:
                if first:
                    first = False

                    prevspace = space
                    space = 0
                    continue
                elif second:
                    second = False

                    prevspace = space
                    space = 0
                else:
                    if prevspace != space:
                        print(f"{counter} NOT EVEN")
                        toNext = True
                        break
                continue

            if prevspace != space:
                print(f"{counter} NOT EVEN")
                toNext = True
                break
                
            prevspace = space
            space = 0

        else:
            whitePixels += 1
            space += 1
        
    if toNext == False:
        print(f"{counter} EVEN")