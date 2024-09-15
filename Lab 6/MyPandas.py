#I'm working with data, interpreted this way:
# [
#      {"TableName1": value0_1,   "TableName2": value0_2,   ...},
#      {"TableName1": value1_1,   "TableName2": value1_2,   ...},
#      ...
# ]

def to_json(path="/") -> list[dict]:
    import csv
    with open(path, "r", encoding="utf-8") as file:
        data = list(csv.DictReader(file))
    return data

def show(data: list[dict], param="top", num=5, separator=", ") -> None:
    #Just checking if user is doing everything correctly
    if type(num) != type(5):
        raise f"TypeError: 'num' arguement must be integer, not {str(type(num))}"
    if type(separator) != type(", "):
        raise f"TypeError: 'separator' arguement must be string, not {str(type(separator))}"
    #? Logical? Yeap, of course)
    if len(data) < num:
        print(f"The length of data is smaller, than the length of num: {len(data)} < {num}")
        print(f"The whole data will be shown.")
        num = len(data)
    #Printing the names of the .csv table
    print(separator.join(map(str, data[0].keys())))
    match param:
        case "top":
            #Writing top (num) values
            for i in range(num):
                print(separator.join(map(str, data[i].values())))
        case "bottom":
            #Writing bottom (num) values
            for i in range(num):
                print(separator.join(map(str, data[0 - i].values())))
        case "random":
            from random import randint
            # To prevent programm from getting the exact same data a couple of tymes randomly 
            # I just add every chosen index to a set structure, until this set with only unique 
            # chosen data length is equal to what I need. And because of this realisation I neeeded
            # to optimise it a bit, because choosing randomly (every time) 999 values from 1000 is, you know,
            # a bit slower than choosing just 1 value from this 1000... 
            already = list()
            if num > len(data) // 2:
                num = data - num
                while len(already) < num:
                    new = randint(0, len(data))
                    if new in already:
                        continue
                    already.append(new) 
                already.sort()
                #Finally printing those random values
                for i in range(len(data)):
                    if not i in already:
                        print(separator.join(map(str, data[i].values())))
                return
            while len(already) < num:
                new = randint(0, len(data))
                if new in already:
                    continue
                already.append(new) 
            already.sort()
            #Finally printing those random values
            for i in already:
                print(separator.join(map(str, data[i].values())))
        case _:
            #If user has done something wrong
            raise "In 'show()' in arguement 'type': type can only be 'top', 'bottom' or 'random'"
        
# Just a simple crutch, because Python don't really want to understand, 
# which type value from str type really is.
# Function uses "trial and error method" :)
def __type_detection(item: str) -> str:
    try:
        temp = int(item)
        return "int"
    except: pass
    try:
        temp = float(item)
        return "float"
    except: pass
    return "str"

    
def info(data: list[dict]) -> None:
    print(f"Size of the table: {len(data)} x {len(data[0].keys())}")
    # Creating dictionary, that will save the amount of not NaN values
    notNaN = dict.fromkeys(list(data[0].keys()), 0)
    # Creating dictionary, that will contain, how many values of which 
    # type each column in table contains
    types = {}
    # Preparing types dictionary
    for key, val in data[0].items():
        types.update({key: {__type_detection(val): 1}})
    # Getting types of each value from each column and checking, if they are NaN
    #TODO Probably in need of optimisation
    for row in data:
        for key, value in row.items():
            notNaN[key] += (1 if (value != "") else 0)
            curtype = __type_detection(value)
            if not curtype in types[key].keys():
                types[key][curtype] = 0
            types[key][curtype] += 1
    # I'm using zip() to correctly get data from the connected parts of data structures
    for (keyNotNaN, valNotNaN), (dataTypes) in zip(notNaN.items(), types.values()):
        # I need to print: name of the column, amount of not NaN values and the type, which most of those values has
        # I'm using ljust to split data and sorting to get the most frequent value type (because of structure of types 
        # dictionary I need to use special sorting key)
        print(str(keyNotNaN).ljust(15), str(valNotNaN).ljust(8), sorted(dataTypes, key=lambda x: dataTypes[x], reverse=True)[0])

def delNaN(data: list[dict]) -> list[dict]:
    # Here I simply delete rows with any NaN values in them
    # using while cycle 'cause the length of data is always changing
    i = 0
    while i < len(data) :
        if any(val == "" for val in data[i].values()):
            data.pop(i)
            i -= 1
        i += 1
    return data

def makeDS(data: list[dict], test_percent = 0.3)  -> None:
    import random, csv, os
    # Here I create directories, if they don't eist already
    if not os.path.exists("train"):
        os.makedirs("train")
    if not os.path.exists("test"):
        os.makedirs("test")
    # I am using the same strategy, as in show(type="random")
    test_nums = set()
    while (len(test_nums) < int(len(data) * test_percent)):
        test_nums.add(random.randint(0, len(data) - 1))
    # Opening\creating files. Newline parameter gets rid of extra blank lines 
    # ('cause writerow method already adds "\n")
    with open("train/train.csv", 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for index, line in enumerate(data):
            if not index in test_nums:
                writer.writerow(line.values())
    with open("test/test.csv", 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for index in test_nums:
            writer.writerow(data[index].values())