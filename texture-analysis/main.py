import sys

while True:
    line = input()

    toNext = False

    whitePixels, blackPixels, prevspace, space = 0, 0, 0, 0

    if line == "END":
        sys.exit()

    for i in line:
        if i == "*":
            blackPixels += 1

            if prevspace != 0 and prevspace != space:
                print("NOT EVEN")
                toNext = True
                break
                
            prevspace = space
            space = 0

        else:
            whitePixels += 1
            space += 1
        
    if toNext == False:
        print("EVEN")