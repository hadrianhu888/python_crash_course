import unittest
import city_functions
from city_functions import *

class CitiesTestCase(unittest.TestCase):    
    def test_get_city_names(self):
        """Try a city like Toronto"""
        city = 'toronto'
        city_expected = f"{city}".title()
        city_format = get_city_name(city)
        self.assertEquals(city_format, city_expected)
    
    def test_get_country_names(self):
        """Try a country like Canada"""       
        country = 'canada'
        country_expected = f"{country}".title()
        country_format = get_country_name(country)
        self.assertEquals(country_format, country_expected)
        
    def test_get_population(self):
        """Try a population of 3800000000"""
        population = '3800000000'
        population_expected = f"{population}".title()
        population_format = get_population(population)
        self.assertEquals(population_format, population_expected)
        
    def test_set_city_country_population(self):
        city = 'toronto'
        country = 'canada'
        population = '3800000000'
        city_country_population_format = set_city_country_population(city, country, population)
        city_country_population_expected = f"{city}, {country}, {population}".title()
        self.assertEquals(city_country_population_format, city_country_population_expected)
        
if __name__ == '__main__':
    unittest.main()
    
