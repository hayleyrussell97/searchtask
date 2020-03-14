import requests

def recipe_search(includeIngredients, cuisine, maxReadyTime, intolerances):
    api_key = 'b6ffea87bb554add8e016a2b945ada6b'
    result = requests.get('https://api.spoonacular.com/recipes/complexSearch?apiKey={}&includeIngredients={}&cuisine={}&maxReadyTime={}&intolerances={}'.format(api_key, includeIngredients, cuisine, maxReadyTime, intolerances))
    data = result.json()
    return data['results']

def run():
    includeIngredients = input('Enter an ingredient: ')
    maxReadyTime = input('How much time do you have to cook? (mins) :')
    cuisine = input('Enter a type of cuisine: ')
    hasintolerances = input('Do you have any intolerances? y/n')
    if hasintolerances == 'y':
        intolerances = input('What is your intolerance?')
    else:
        intolerances = ''

    recipes = recipe_search(includeIngredients, cuisine, maxReadyTime, intolerances)

    for recipe in recipes:
        print(recipe['title'])

run()