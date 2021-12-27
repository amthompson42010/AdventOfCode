def readFile():
    data = []
    f = open("../data/2_data.txt", "r")
    for x in f:
        if(x != ""):
            if "\n" not in x:
                data.append(x)
            else:
                data.append(x[:-1])
    return data

def analyzeData(data):
    validCount = 0
    for item in data:
        newData = item.split("-")
        first_limit = newData[0]
        newDataPartTwo = newData[1].split(":")
        heart = newDataPartTwo[1][1:]
        break_further = newDataPartTwo[0].split(" ")
        second_limit = break_further[0]
        letter = break_further[1]

        isValid = validate(first_limit, second_limit, letter, heart)
        if(isValid == True):
            validCount += 1
        else:
            validCount = validCount

    return validCount

def validate(first_limit, second_limit, letter, pw):
    return (pw[int(first_limit) - 1] == letter) != (pw[int(second_limit) - 1] == letter)

def main():
    file_contents = readFile()
    result = analyzeData(file_contents)
    print("# of valid passwords: {}".format(result))

if __name__ == "__main__":
    main()