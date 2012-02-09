import unittest
import Recipe
from IngredientParser import IngredientParser

class TestRecipeFunctions(unittest.TestCase):
    
    def testNonsenseIsNone(self):
    	self.assertIsNone(Recipe.FetchRecipe("nonsense url"))
    
    def testIngrediantsList(self):
		self.chick_salad_recipe = Recipe.FetchRecipe("http://allrecipes.com/recipe/holiday-chicken-salad/detail.aspx")
		self.assertIsNotNone(self.chick_salad_recipe);
		self.assertIs(type(self.chick_salad_recipe.ingredients), list);
		self.assertIs(self.chick_salad_recipe.ingredients[0].__class__, Recipe.Ingredient);


class TestIngredientParsing(unittest.TestCase):

	def testIngrediantParserWords(self):
		ingparser = IngredientParser()
		self.assertIs(ingparser.ingredients_list.count("onion"), 1)
		self.assertIs(ingparser.unit_list.count("tablespoon"), 1)


if __name__ == '__main__':
    unittest.main()
