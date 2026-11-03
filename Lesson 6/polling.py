favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

friends = ['jen', 'cipi', 'sarah', 'parpi', 'edward', 'capy', 'phil']

for name in friends:
    print(f"Hi {name.title()}.")

    if name in favourite_languages.keys():
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")
    else:
        print("Please take the poll!")