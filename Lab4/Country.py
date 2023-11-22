class Country:
    def __init__(self, name, capital, area, population):
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population

def countries_by_area(min_area, max_area):
    return [country for country in countries if min_area <= country.area <= max_area]

def countries_by_population(min_population, max_population):
    return [country for country in countries if min_population <= country.population <= max_population]

countries = [
    Country("USA", "Washington, D.C.", 9833517, 331_915_073),
    Country("China", "Beijing", 9596961, 1_444_216_107),
    Country("India", "New Delhi", 3287263, 1_393_409_038),
    Country("Russia", "Moscow", 17125242, 145_912_025),
    Country("Brazil", "Brasília", 8515767, 212_559_417)
]

min_area = 5000000
max_area = 10000000  

print(f"Страны с площадью от {min_area} до {max_area} кв. км:")

for country in countries_by_area(min_area, max_area):
    print(f"{country.name}: {country.area} кв. км")

min_population = 100_000_000
max_population = 1_000_000_000

print(f"Страны с численностью населения от {min_population} до {max_population}:")
for country in countries_by_population(min_population, max_population):
    print(f"{country.name}: {country.population} человек")