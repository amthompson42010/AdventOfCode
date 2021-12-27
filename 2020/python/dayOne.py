from itertools import combinations

def getData():
    data = []
    f = open("../data/1_data.txt", "r")
    for x in f:
        if(x != ""):
            if "\n" not in x:
                data.append(int(x))
            else:
                data.append(int(x[:-1]))
    return data

def getResult(data_source):
    data = list(combinations(data_source, 3))
    for item in data:
        sumValue = item[0] + item[1] + item[2]
        if(sumValue == 2020):
            resultValues = list((item[0], item[1]))
            result = item[0] * item[1] * item[2]
        else:
            continue
    return result

def main():
    data_source = getData()
    result = getResult(data_source)
    print("{}".format(result))

if __name__ == "__main__":
    main()