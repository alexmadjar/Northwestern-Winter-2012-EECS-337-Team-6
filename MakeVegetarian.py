import Recipe
import sys

recipe_url = raw_input('allrecipes.com full url: ')
recipy = Recipe.FetchRecipe(recipe_url)
if recipy is None:
	print '\033[1;38mThere was an error fetching that recipe\033[1;m'
	print '\tPlease check the url'
	sys.exit(0)
print '\n\n\n\nThe Original Recipe:\n'
Recipe.PrintRecipe(recipy)
print '\n\n\n\n'
print 'The Vegetarian Version:\n'
veggie = Recipe.VegetarianVersion(recipy)
Recipe.PrintRecipe(veggie)
 