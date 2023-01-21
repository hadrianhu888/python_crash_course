def get_city_name(city):
    """Gets a city name"""    
    city_format = f"{city}"
    return city_format.title()

def get_country_name(country):
    """Gets a country name"""    
    country_format = f"{country}"
    return country_format.title()

def get_population(population):
    """Gets a population number"""    
    population_format = f"{population}"
    return population_format.title()

def set_city_country_population(city,country,population):
    city_country_population_format = f"{city}, {country}, {population}"
    return city_country_population_format.title()

