countries = input().split(", ")
capitals = input().split(", ")

geo_dict = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in geo_dict.items():
    print(f"{country} -> {capital}")