def taxicab(p1, p2, q1, q2):
    temp = p1 - q1
    temp2 = p2 - q2
    if(temp < 0):
        temp = temp * -1
    if(temp2 < 0):
        temp2 = temp2 * -1
    
    return temp + temp2

def move(wire, x, y):
    points = [] 
    for i in range(len(wire)):
        temp = wire[i]
        if(temp[0] == "R"):
            for i in range(int(temp[1:])):
                y += 1     
                points.append(str(x)+" "+str(y))           
        if(temp[0] == "U"):
            for i in range(int(temp[1:])):
                x += -1    
                points.append(str(x)+" "+str(y))
        if(temp[0] == "L"):
            for i in range(int(temp[1:])):
                y += -1     
                points.append(str(x)+" "+str(y))                
        if(temp[0] == "D"):
            for i in range(int(temp[1:])):
                x += 1     
                points.append(str(x)+" "+str(y)) 
    
    return points

def manhattan(value):
    one = value[0].split(",")
    two = value[1].split(",")

    x = 50
    y = 50

    pointsA =  move(one, x, y)
    pointsB =  move(two, x, y) 

    minValue = 100000000000
    
    for p in pointsA:
        if(p in pointsB):
            value = p.split(" ")
            result = taxicab(int(value[0]), int(value[1]), x, y)
            if(result < minValue):
                minValue = result
    print(minValue)   

def readfile(path):
    with open(path, 'r+') as file:
        text = file.read()
        text = text.rstrip()
        return text.split("\n")

def execute():
    manhattan(readfile("files//day-three.txt"))
    #manhattan(readfile("files//test.txt"))


execute()
