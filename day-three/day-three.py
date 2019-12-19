

def printMatrix(matrix):    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                #matrix[i][j] = " . "
                print(matrix[i][j], end='')
        print()

def taxicab(p1, p2, q1, q2):
    temp = p1 - q1
    temp2 = p2 - q2
    if(temp < 0):
        temp = temp * -1
    if(temp2 < 0):
        temp2 = temp2 * -1
    
    return temp + temp2

def move(matrix, wire, x, y):
    points = [] 
    for i in range(len(wire)):
        temp = wire[i]
        if(temp[0] == "R"):
            for i in range(int(temp[1:])):
                y += 1 
                matrix[x][y] = " - "    
                points.append(str(x)+" "+str(y))           
        if(temp[0] == "U"):
            for i in range(int(temp[1:])):
                x += -1
                matrix[x][y] = " | "    
                points.append(str(x)+" "+str(y))
        if(temp[0] == "L"):
            for i in range(int(temp[1:])):
                y += -1 
                matrix[x][y] = " - "    
                points.append(str(x)+" "+str(y))                
        if(temp[0] == "D"):
            for i in range(int(temp[1:])):
                x += +1
                matrix[x][y] = " | "     
                points.append(str(x)+" "+str(y)) 
    
    return points

def manhattan(value):
    one = value[0].split(",")
    two = value[1].split(",")
    print(one)
    print(two)
    r = 0
    u = 0
    l = 0
    d = 0

    for i in range(len(one)):
        temp = one[i]
        if(temp[0] == "R"):
            r = int(temp[1:])
        if(temp[0] == "U"):
            u = int(temp[1:])
        if(temp[0] == "D"):
            d = int(temp[1:])
        if(temp[0] == "L"):
            l = int(temp[1:])
    
    for i in range(len(two)):
        temp = two[i]
        if(temp[0] == "R"):
            r += int(temp[1:])
        if(temp[0] == "U"):
            u += int(temp[1:])
        if(temp[0] == "D"):
            d += int(temp[1:])
        if(temp[0] == "L"):
            l += int(temp[1:])


    w, h = (r+l), (u+d);
    matrix = [[0 for x in range(w)] for y in range(h)] 
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                matrix[i][j] = " . "
                #print(matrix[i][j], end='')
        #print()

    matrix[int(w/2)][int(h/2)] = " o "

    x = int(w/2)
    y = int(h/2)

    matrix[x][y] = " o "

    pointsA =  move(matrix, one, x, y)
    pointsB =  move(matrix, two, x, y) 

    minValue = 100000000000
    
    for p in pointsA:
        if(p in pointsB):
            value = p.split(" ")
            result = taxicab(int(value[0]), int(value[1]), x, y)
            if(result < minValue):
                minValue = result
    print(minValue)
   

    printMatrix(matrix)

def readfile(path):
    with open(path, 'r+') as file:
        text = file.read()
        text = text.rstrip()
        return text.split("\n")

def execute():
    #manhattan(readfile("files//day-three.txt"))
    manhattan(readfile("files//test.txt"))


execute()
