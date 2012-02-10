import Recipe
from fractions import Fraction

def comparebylength(word1, word2):
    """
    write your own compare function:
    returns value < 0 of word1 longer then word2
    returns value = 0 if the same length
    returns value > 0 of word2 longer than word1
    """
    return len(word2) - len(word1)

def removeParentheticals(t):
    """
    removes parenthetical statements from t
    NOTE: fails on nested parentheticals
    """
    while t.find('(') != -1:
        (p, m, n) = t.partition('(')
        (m, d, n) = n.partition(')')
        t = p + n
    return t

def returnFirstMatch(str, bank):
	"""
	returns the first string in bank that is a substring of str
	"""
	for s in bank:
		if str.find(s) != -1:
			return s
	return ""

class IngredientParser:
	ingredients_list = []
	unit_list = []
	def __init__(self):
		ingredients_file = open("ingredients.txt")
		for line in ingredients_file:
			self.ingredients_list.append(line.strip())
		# dedupe the list
		self.ingredients_list = list(set(self.ingredients_list))
		# sort it by length for greedy string matching algorithm
		self.ingredients_list.sort(cmp=comparebylength)
		units_file = open("units.txt")
		for line in units_file:
			self.unit_list.append(line.strip())
	
	def CreateIngredientFromString(self, str):
		ret = Recipe.Ingredient()
		str = removeParentheticals(str) + " "
		str_toks = str.split(" ")
		try:
			ret.quantity = float(Fraction(str_toks[0]))
			ret.quantity += float(Fraction(str_toks[1]))
		except ValueError:
			pass
		rin = returnFirstMatch(str, self.ingredients_list).strip()
		if rin != '':
			ret.name = rin
		rin = returnFirstMatch(str, self.unit_list).strip()
		if rin != '':
			ret.unit = rin
		return ret
