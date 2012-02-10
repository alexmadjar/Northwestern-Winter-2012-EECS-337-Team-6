from BeautifulSoup import BeautifulSoup
import urllib2
import re
import IngredientParser

class Recipe:
    ingredients = []
    directions = []

class Ingredient:
        quantity = 0 #e.g. 1
        unit = '' #e.g. tablespoon
        #meat = False
        name = '' #e.g. salt
        
def FetchRecipe(url):
    try:
        usock = urllib2.urlopen(url)
        html_data = usock.read()
        usock.close()
    except ValueError:
        return None
     
    #Create the soup object from the HTML data
    soup = BeautifulSoup(html_data)
    recipeFromURL = Recipe()
    
    ingredient_tags = soup.findAll('li',attrs={"class" : "plaincharacterwrap ingredient"})
    ingredients = [tag.contents[0] for tag in ingredient_tags]
    
    #Format the ingredients to remove \r\n and leading spaces 
    #Assign the formatted ingredients to 
    regex = '\\r\\n.[ ]+'
    ingparser = IngredientParser.IngredientParser()
    for ingredient_name in ingredients:
        recipeFromURL.ingredients.append(
           ingparser.CreateIngredientFromString(
              re.sub(regex, '', ingredient_name)
            )
         )
    
    #Directions
    directions_tags = soup.findAll('div', attrs={"class" : "directions"})
    directions_tags = directions_tags[0]('span', attrs={"class" : "plaincharacterwrap break"})
    directions = [tag.contents[0] for tag in directions_tags]
    regex = '\\r\\n.[ ]+'
    for step_in_directions in directions:
        print step_in_directions
        recipeFromURL.directions.append(
              re.sub(regex, '', step_in_directions)
            )

    return recipeFromURL
    

def PrintRecipe(recipe):
    print recipe.ingredients
    print recipe.directions
    return None


def VegetarianVersion(recipe):
    #Version 1: Replace the meat ingredients with a random vegitarian substitute
    
    return recipe

