from BeautifulSoup import BeautifulSoup
import urllib2
import re
import IngredientParser

class Recipe:
    ingredients = []

class Ingredient:
        quantity = 0 #e.g. 1
        unit = 'unit' #e.g. tablespoon
        #meat = False
        name = 'unknown' #e.g. salt
        
def FetchRecipe(url):
    try:
        usock = urllib2.urlopen(url)
        html_data = usock.read()
        usock.close()
    except ValueError:
        return None
     
    #Create the soup object from the HTML data
    soup = BeautifulSoup(html_data)
    
    ingredient_tags = soup.findAll('li',attrs={"class" : "plaincharacterwrap ingredient"})
    
    recipeFromURL = Recipe()
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

    return recipeFromURL
    

def PrintRecipe(recipy):
    print recipy.ingredients
    return None


def VegetarianVersion(recipy):
    return recipy

