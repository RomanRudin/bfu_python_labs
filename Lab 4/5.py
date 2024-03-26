from random import randint

words = ['Карандаш', 'Маркер', 'Тетрадь', 'Линейка', 'Ручка', 'Скотч', 'КлейПВА', 'Ластик', 'Мел']

data = {}

def save_info(customer_id, commodity, number):
        if not customer_id in data.keys():
            data[customer_id] = {}
        if not commodity in  data[customer_id].keys():
            data[customer_id][commodity] = number
        else:
            data[customer_id][commodity] += number

def generate(n):
    num_customers = randint(1, int(n ** 0.5))
    print("Number of customers:", num_customers)
    print("Transactions")
    for i in range(n):
        customer_id = randint(1, num_customers)
        commodity = words[randint(0, len(words) - 1)]
        number = randint(1, int(n ** 0.5))
        print(f'{i + 1})\t {customer_id} {commodity} {number}')
        save_info(customer_id, commodity, number)

generate_data = True
n = int(input("Please, enter the number: "))
if not generate_data:
    for i in range(n):
        line = input().strip().split()
        save_info(line[0], line[1], int(line[2]))
else:
    generate(n)
for customer in data.keys():
    print(f'Customer №{customer}:')
    for commodity, number in data[customer].items():
        print(f"\t {commodity}: {number}")