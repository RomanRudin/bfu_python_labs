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
        
def info(data: list[dict]) -> None:
    print(f"Size of the table: {len(data)} x {len(data[0].keys())}")
    notNaN = dict.fromkeys(list(data[0].keys()), 0)
    for row in data:
        for key, value in row.items():
            notNaN[key] += 1 if (value != "") else 0
    for key, val in notNaN.items():
        print(str(key).ljust(15), str(val).ljust(8), str(type(data[0][key])).removeprefix("<class '").removesuffix("'>"))

def delNaN(data: list[dict]) -> list[dict]:
    for index, row in enumerate(data):
        if any([val == "" or val == " " for val in row.values()]):
            data.pop(index)
    return data

def makeDS(data: list[dict])  -> None:
    import random
    pass