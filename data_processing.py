import csv
import os

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


def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps


def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)

avg_float = lambda seq: (sum(map(float, seq)) / len(seq))
max_float = lambda seq: max(map(float, seq))

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
print("All cities in Germany")
filtered_list = filter(lambda x: x['country'] == 'Germany', cities)
print(filtered_list)
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C")
spain_filtered = filter(lambda x: x['country'] == 'Spain' and float(
    x['temperature']) > 12, cities)
print(spain_filtered)
print()

# Count the number of unique countries
print("number of unique countries")
unique_country_count = aggregate("country", lambda lst: len(set(lst)), cities)
print(unique_country_count)
print()


# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany")
print(f"{aggregate("temperature", avg_float, cities)}")
print()

# Print the max temperature for all the cities in Italy
print("max temperature for all the cities in Italy")
italy_cities = filter(lambda x: x["country"] == "Italy", cities)
print(aggregate("temperature", max_float, italy_cities))
