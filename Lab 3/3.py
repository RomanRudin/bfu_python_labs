data = input("Please, enter the integer: ")
assert data.isalnum()
assert 0 < int(data) < 1000 
answer = ""
if len(data) == 3:
    match int(data[0]):
        case 1: answer += "сто "
        case 2: answer += "двести "
        case 3: answer += "триста "
        case 4: answer += "четыреста "
        case 5: answer += "пятьсот "
        case 6: answer += "шестьсот "
        case 7: answer += "семьсот "
        case 8: answer += "восемьсот "
        case 9: answer += "девятьсот "
    data = data[1:]
if len(data) == 2:
    match int(data[0]):
        case 0: answer += ""
        case 1: 
            match int(data[1]):
                case 0: answer += "десять "
                case 1: answer += "одиннадцать "
                case 2: answer += "двенадцать "
                case 3: answer += "тринадцать "
                case 4: answer += "четырнадцать "
                case 5: answer += "пятнадцать "
                case 6: answer += "шестнадцать "
                case 7: answer += "семнадцать "
                case 8: answer += "восемнадцать "
                case 9: answer += "девятнадцать "
            data = data[1:]
        case 2: answer += "двадцать "
        case 3: answer += "тридцать "
        case 4: answer += "сорок "
        case 5: answer += "пятьдесят "
        case 6: answer += "шестьдесят "
        case 7: answer += "семьдесят "
        case 8: answer += "восемьдесят "
        case 9: answer += "девяносто "
    data = data[1:]
if len(data) == 1:
    match int(data):
        case 0: answer += ""
        case 1: answer += "один"
        case 2: answer += "два"
        case 3: answer += "три"
        case 4: answer += "четыре"
        case 5: answer += "пять"
        case 6: answer += "шесть"
        case 7: answer += "семь"
        case 8: answer += "восемь"
        case 9: answer += "девять"
print(f"this integer is {answer.capitalize()} in Russian")