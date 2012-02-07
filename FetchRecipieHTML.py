from BeautifulSoup import BeautifulSoup
import urllib2
import re

class Recipe:
    ingredients = []
#class Ingredient:
        #quantity = 0 #e.g. 1
        #units = 0
        #meat = False
        #name = ''
        
def FetchRecipie(url):
    usock = urllib2.urlopen(url)
    html_data = usock.read()
    usock.close()
    #print html_data
     
    #Create the soup object from the HTML data
    soup = BeautifulSoup(html_data)
    
    ingredient_tags = soup.findAll('li',attrs={"class" : "plaincharacterwrap ingredient"})
    
    recipeFromURL = Recipe()
    ingredients = [tag.contents[0] for tag in ingredient_tags]
    
    #Format the ingredients to remove \r\n and leading spaces 
    #Assign the formatted ingredients to 
    regex = '\\r\\n.[ ]+'
    for ingredient_name in ingredients:
        recipeFromURL.ingredients.append(re.sub(regex, '', ingredient_name))
        
    print recipeFromURL.ingredients
    return recipeFromURL
####

url = 'http://allrecipes.com/Recipe/Best-Tuna-Casserole/Detail.aspx'
FetchRecipie(url)
    