#Необходимо создать три словаря и написать функцию, которая сможет брать словари и производить их слияние в один
capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
cars = {'red': 2, 'black': 10, 'green': 4}
months = {'January': 1, 'February': 2, 'March': 3}
print(capitals)
print(cars)
print(months)

def merge(f, s, t):
    return { **f, **s, **t }
print("Final_: ", merge(capitals, cars, months))
