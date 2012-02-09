import Recipe

def comparebylength(word1, word2):
    """
    write your own compare function:
    returns value < 0 of word1 longer then word2
    returns value = 0 if the same length
    returns value > 0 of word2 longer than word1
    """
    return len(word2) - len(word1)

class IngredientParser:
	ingredients_list = []
	unit_list = []
	def __init__(self):
		ingredients_file = open("ingredients.txt")
		for line in ingredients_file:
			self.ingredients_list.append(line.strip())
		self.ingredients_list = list(set(self.ingredients_list))
		self.ingredients_list.sort(cmp=comparebylength)
		units_file = open("units.txt")
		for line in units_file:
			self.unit_list.append(line.strip())
	
	def CreateIngredientFromString(self, str):
		return Recipe.Ingredient() 
