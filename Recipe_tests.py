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
	def setUp(self):
		self.ingparser = IngredientParser()

	def testIngrediantParserWords(self):
		self.assertIs(self.ingparser.ingredients_list.count("onion"), 1)
		self.assertIs(self.ingparser.ingredients_list.count("ounce"), 0)
		self.assertIs(self.ingparser.unit_list.count("tablespoon"), 1)
		self.assertIs(self.ingparser.unit_list.count("sausage"), 0)
	
	# test cases to add

	# 4 cups cubed, cooked chicken meat',
	# u'1 cup mayonnaise',
	# u'1 teaspoon paprika',
	# u'1 1/2 cups dried cranberries',
	# u'1 cup chopped celery',
	# u'1/2 cup minced green bell pepper',
	# u'1 cup chopped pecans',
	# u'1 teaspoon seasoning salt',
	# u'ground black pepper to taste

	def testIngrediantParsingSeasoningSalt(self):
		ing = self.ingparser.CreateIngredientFromString(u'1 teaspoon seasoning salt')
		self.assertTrue(abs(ing.quantity - float(1)) < 0.0000001) 
		self.assertEqual(ing.unit, 'teaspoon')
		self.assertEqual(ing.name, 'seasoning salt')
	
	def testIngredientParseGreenOnions(self):
		ing = self.ingparser.CreateIngredientFromString(u'2 green onions, chopped')
		self.assertTrue(abs(ing.quantity - float(2)) < 0.0000001) 
		self.assertEqual(ing.unit, 'unit')
		self.assertEqual(ing.name, 'green onion')


if __name__ == '__main__':
    unittest.main()
