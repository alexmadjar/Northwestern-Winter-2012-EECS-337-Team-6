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
		self.assertTrue(self.ingparser.isIngredient("chicken"))
		self.assertTrue(self.ingparser.isIngredient("salt"))
		self.assertFalse(self.ingparser.isIngredient("tablespoon"))
		self.assertTrue(self.ingparser.isUnit("ounce"))
		self.assertFalse(self.ingparser.isUnit("veal"))
	
	# test cases to add
	# u'ground black pepper to taste

	def ingredientParserHelper(self, st, quan, uni, nam, ismeat):
		ing = self.ingparser.CreateIngredientFromString(st)
		self.assertTrue(abs(ing.quantity - float(quan) < 0.0000001) )
		self.assertEqual(ing.unit, uni)
		self.assertEqual(ing.name, nam)
		self.assertTrue(ing.meat == ismeat)
	
	def testPaprika(self):
		self.ingredientParserHelper(u'1 teaspoon paprika', 1, "teaspoon", "paprika", False)

	def testIngrediantParsingSeasoningSalt(self):
		self.ingredientParserHelper(u'1 teaspoon seasoning salt', 1, "teaspoon", "seasoning salt", False)
	
	def testIngredientParseGreenOnions(self):
		self.ingredientParserHelper(u'2 green onions, chopped', 2, "unit", "green onion", False)

	def testChickenCookedAndCubed(self):
		self.ingredientParserHelper(u'4 cups cubed, cooked chicken meat', 4, "cup", "chicken", True)
	
	def testHalfIngredient(self):
		self.ingredientParserHelper(u'1/2 cup minced green bell pepper', 0.5, "cup", "green bell pepper", False)
	
	def testMixedFraction(self):
		self.ingredientParserHelper(u'1 1/2 cups dried cranberries', 1.5, "cup", "cranberries", False)
	
	def testToTaste(self):
		self.ingredientParserHelper(u'ground black pepper to taste', 1.0, "to taste", "black pepper", False)

if __name__ == '__main__':
	unittest.main()
