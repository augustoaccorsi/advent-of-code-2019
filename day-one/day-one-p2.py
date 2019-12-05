def fuelsum(path):
    with open(path, 'r+') as file:
        text = file.read()
        text = text.rstrip()
        value = text.split("\n")
        
        result = 0

        for val in value:
            value = int(int(val)/3)-2
            result += value
            while(value > 0):
                value = int(int(value)/3)-2
                if(value > 0):              
                    result += value

        print(result)

fuelsum("..//files//day-one.txt")