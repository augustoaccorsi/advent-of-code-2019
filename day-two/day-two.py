def alarm(value):
    #  2,3,0,3,99
    print(value)

    value[1] = 12
    value[2] = 2

    for i in range(0,len(value),4):
       # [1, 9, 10, 3,
       #  2, 3, 11, 0,
       #  99, 30, 40, 50]
        try:

            if(value[i] == 2):
                value[value[i+3]] = value[value[i+1]] * value[value[i+2]]
                print("dois")

            if(value[i] == 1):
                value[value[i+3]] = value[value[i+1]] + value[value[i+2]]
                print("um")

            if(value[i] == 99):
                print(value)
                return value[0]

        except:
            print("err")
            return value[0]
        

    #return value[0]

def readfile(path):
    with open(path, 'r+') as file:
        text = file.read()
        value = text.split(",")

        valint = []

        for i in range(len(value)):
            valint.append(int(value[i]))
           # print(int(value[i]))

        print(alarm(valint))

#readfile("files//test.txt")
readfile("files//day-two.txt")