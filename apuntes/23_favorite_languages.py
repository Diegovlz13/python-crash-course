favorite_languages = {
    'jen': ['python', 'java'],
    'sarah': ['c', 'c++'],
    'edward': ['ruby', 'java'],
    'phil': ['c#', 'python'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")
