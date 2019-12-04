def fuelsum(path):
    with open(path, 'r+') as file:
        text = file.read()
        text = text.rstrip()
        value = text.split("\n")
        
        result = 0

        for val in value:
           result += int(int(val)/3)-2

        print(result)

fuelsum("..//files//day-one.txt")