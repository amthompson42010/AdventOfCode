def checkIncrement(results):

    decreased = 0
    increased = 0
    trash = 0
    current = 0

    for x in results:
        if current < x and current > 0:
            increased = increased + 1
        elif current > x:
            decreased = decreased + 1
        else:
            trash = trash + 1
        current = x

    return increased

def main():
    tempCount = 0
    tempValue = 0
    oldValues = []
    valuesToCompare = []
    results = []
    f = open("input.txt", "r")
    for x in f:
        print("[x]: ", x)
        if tempCount % 3 != 0:
            print("hit non 3")
            valuesToCompare.append(int(x))
            
            if tempCount = 2:
                oldValues.append(int(x))
            
            tempCount = tempCount + 1
        else:
            print("[valuesToCompare]: ", valuesToCompare)
            for i in valuesToCompare:
                tempValue = tempValue + i
            results.append(tempValue)
            
            valuesToCompare = 
            oldValues = []
            tempValue = 0
    
    numberIncreased = checkIncrement(results)

    print("[result]: ", results)
    print("number: ", numberIncreased)

    #print("total increased: ", increased)

main()
