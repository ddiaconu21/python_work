cities = {
    'Craiova': {

        'Country': 'Romania', 
        'Population': '300k',
        'Fact': 'Known for using a specific past tense',
    },
    'Bucharest': {
        'Country': 'Romania',
        'Population': '4M',
        'Fact': 'All the people around the country come here',
    },
    'Cluj': {

        'Country': 'Romania', 
        'Population': '1M', 
        'Fact': 'Most expensive city in Romania',
    }
}

for name, info in cities.items():
    country = info['Country']
    population = info['Population']
    fact = info['Fact']

    print(f"The city {name.title()} is in {country}.")
    print(f"The population of {name.title()} is {population}.")
    print(f"A fun fact about {name.title()} is {fact}.")