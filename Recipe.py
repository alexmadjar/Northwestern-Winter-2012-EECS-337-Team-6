from BeautifulSoup import BeautifulSoup
import urllib2
import re
import IngredientParser

class Recipe:
    ingredients = []
    directions = []

class Ingredient:
        quantity = 1.0 #e.g. 1
        unit = 'unit' #e.g. tablespoon
        meat = False
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
              re.sub(regex, '', ingredient_name).lower()
            )
         )
    #Directions
    directions_tags = soup.findAll('div', attrs={"class" : "directions"})
    directions_tags = directions_tags[0]('span', attrs={"class" : "plaincharacterwrap break"})
    directions = [tag.contents[0] for tag in directions_tags]
    regex = '\\r\\n.[ ]+'
    for step_in_directions in directions:
        recipeFromURL.directions.append(
              re.sub(regex, '', step_in_directions).lower()
            )
    return recipeFromURL
    

def PrintRecipe(recipe):
    print 'INGREDIENTS\n',
    print '-------------\n',
    for cur_ingredient in recipe.ingredients:
        print 'Quantity:',
        print cur_ingredient.quantity,
        print 'Unit:',
        print cur_ingredient.unit,
        print 'Name:',
        print cur_ingredient.name,
        print 'Meat:' ,
        print cur_ingredient.meat,
        print '\n',
    
    print '\n',
    print 'DIRECTIONS\n',
    print '-------------\n',
    count = 1   
    for cur_direction in recipe.directions:
        print 'Step ',
        print count,
        print ': ',
        print cur_direction,
        print '\n',
        count = count + 1
    return None

def IsVeggie(recipe):
    for ing in recipe.ingredients:
        if ing.meat:
            return False
    return True

def VegetarianVersion(recipe):
    #Replace the meat ingredients with a random vegitarian substitute
    my_dict = eval(open("meats.txt").read())
    #normalize dictionary keys
    for k in my_dict.keys():
        my_dict[k.strip().lower()] = my_dict[k]
    for cur_ingredient in recipe.ingredients:
        if cur_ingredient.meat == True:
            oldname = cur_ingredient.name
            if cur_ingredient.name in my_dict.keys():
                cur_ingredient.name = my_dict[cur_ingredient.name]
            else:
                cur_ingredient.name = 'meatless ' + cur_ingredient.name
            cur_ingredient.meat = False
            #update directions
            new_directions = []
            for d in recipe.directions:
                new_directions.append(d.replace(oldname, cur_ingredient.name))
            recipe.directions = new_directions;
    return recipe

