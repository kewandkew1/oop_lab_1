import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All city in Germany")
germany_city = []
for i in cities:
    if i['country'] == 'Germany':
        germany_city.append(i['city'])

print(germany_city)
print()
    

# Print all cities in Spain with a temperature above 12°C
spain_city = []
print("all cities in Spain with a temperature above 12°C")
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) > 12:
        spain_city.append(city['city'])
print(spain_city)
print()


# Count the number of unique countries
print("number of unique countries")
country_lst = []
for i in cities:
    country_lst.append(i['country'])

print(len(set(country_lst)))
print()
        

# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany")
germany_temp = 0
for i in cities:
    if i['country'] == "Germany":
        germany_temp += float(i['temperature'])
print(f"{germany_temp / len(germany_city):.2f}")
print()

# Print the max temperature for all the cities in Italy
print("max temperature for all the cities in Italy")
italy_temp = []
for i in cities:
    if i['country'] == "Italy":
        italy_temp.append(i['temperature'])
print(max(italy_temp))
        


