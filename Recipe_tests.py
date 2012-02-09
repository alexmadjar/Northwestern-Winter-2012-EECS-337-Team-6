import unittest
import Recipe

class TestSequenceFunctions(unittest.TestCase):
    
    def setUp(self):

    def testNonsenseIsNone(self):
    	self.assertIsNone(Recipe.FetchRecipe("nonsense url"))
    
    def testIngrediantsList(self):
		self.chick_salad_recipe = Recipe.FetchRecipe("http://allrecipes.com/recipe/holiday-chicken-salad/detail.aspx")
		self.assertIsNotNone(self.chick_salad_recipe);
		self.assertIs(type(self.chick_salad_recipe.ingredients), list);
		self.assertIs(type(self.chick_salad_recipe.ingredients[0]), Recipe.Ingredient);


if __name__ == '__main__':
    unittest.main()
