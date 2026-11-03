favourite_places = {
    'Gabi': ['Japan', 'Gym', 'Chicago'],
    'Papi': ['Home', 'Japan', 'Greece'],
    'Dani': ['USA', 'Brussels', 'Romania'],
}

for name, places in favourite_places.items():
    print (f"\n{name.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")