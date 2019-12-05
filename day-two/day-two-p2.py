def alarm(value, noun, verb):
    value[1] = noun
    value[2] = verb

    for i in range(0,len(value),4):
        try:

            if(value[i] == 2):
                value[value[i+3]] = value[value[i+1]] * value[value[i+2]]

            if(value[i] == 1):
                value[value[i+3]] = value[value[i+1]] + value[value[i+2]]

            if(value[i] == 99):
                return value[0]

        except:
            print("err")
            return value[0]

def readfile(path):
    with open(path) as f:
        return list(map(int, f.read().split(',')))

def execute():
    value = readfile("files//day-two.txt")
    for noun in range(100):
        for verb in range(100):
            if(alarm(value.copy(), noun, verb) == 19690720):
                return 100 * noun + verb

print(execute())