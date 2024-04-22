def to_json(path="/") -> list[dict]:
    import csv
    with open(path, "r", encoding="utf-8") as file:
        data = list(csv.DictReader(file))
    return data

def show(data: list[dict], param="top", num=5, separator=", ") -> None:
    if type(num) != type(5):
        raise f"TypeError: 'num' arguement must be integer, not {str(type(num))}"
    if type(separator) != type(", "):
        raise f"TypeError: 'separator' arguement must be string, not {str(type(separator))}"
    if len(data) < num:
        print(f"The length of data is smaller, than the length of num: {len(data)} < {num}")
        print(f"The whole data will be shown.")
        num = len(data)
    print(separator.join(map(str, data[0].keys())))
    match param:
        case "top":
            for i in range(num):
                print(separator.join(map(str, data[i].values())))
        case "bottom":
            for i in range(num):
                print(separator.join(map(str, data[0 - i].values())))
        case "random":
            from random import randint
            already = list()
            if num > len(data) // 2:
                num = data - num
                while len(already) < num:
                    new = randint(0, len(data))
                    if new in already:
                        continue
                    already.append(new) 
                already.sort()
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
            for i in already:
                print(separator.join(map(str, data[i].values())))
        case _:
            raise "In 'show()' in arguement 'type': type can only be 'top', 'bottom' or 'random'"
        
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
    notNaN = dict.fromkeys(list(data[0].keys()), 0)
    types = {}
    for key, val in data[0].items():
        types.update({key: {__type_detection(val): 1}})
    for row in data:
        for key, value in row.items():
            notNaN[key] += 1 if (value != "") else 0
            curtype = __type_detection(value)
            if not curtype in types[key].keys():
                types[key][curtype] = 0
            types[key][curtype] += 1
    for (keyNotNaN, valNotNaN), (dataTypes) in zip(notNaN.items(), types.values()):
        print(str(keyNotNaN).ljust(15), str(valNotNaN).ljust(8), sorted(dataTypes, key=lambda x: dataTypes[x], reverse=True)[0])

def delNaN(data: list[dict]) -> list[dict]:
    i = 0
    while i < len(data) :
        if any(val == "" for val in data[i].values()):
            data.pop(i)
            i -= 1
        i += 1
    return data

def makeDS(data: list[dict], test_percent = 0.3)  -> None:
    import random, csv, os
    if not os.path.exists("train"):
        os.makedirs("train")
    if not os.path.exists("test"):
        os.makedirs("test")
    test_nums = set()
    while (len(test_nums) < int(len(data) * test_percent)):
        test_nums.add(random.randint(0, len(data) - 1))
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