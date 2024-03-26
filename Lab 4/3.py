n = int(input("Please, enter the number of cities: "))
cities = set()
for i in range(n):
    city = input("Please, enter the city: ").strip().lower()
    if city in cities:
        print("REPEAT")
    else:
        cities.add(city)
        print("OK")