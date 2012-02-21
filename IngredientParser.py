import Recipe
from fractions import Fraction

class IngListItem:
	name = ''
	meat = False

	def __init__(self, st, b):
		self.name = st
		self.meat = b

def normalize_string(line):
	return removeParentheticals(line).strip().lower()

def comparebylength(word1, word2):
	"""
	write your own compare function:
	returns value < 0 of word1 longer then word2
	returns value = 0 if the same length
	returns value > 0 of word2 longer than word1
	"""
	return len(word2.name) - len(word1.name)

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

def returnFirstMatch(st, bank):
	"""
	returns the first string in bank that is a substring of str
	"""
	for s in bank:
		if st.find(s.name) != -1:
			return s
	return IngListItem("", False)

def isMeat(str,bank):
	for s in bank:
		if(str == s): 
			return True
	return False
		
class IngredientParser:
	ingredients_list = []
	unit_list = []
	meats_list = []
	
	def __init__(self):
		ingredients_file = open("ingredients.txt")
		for line in ingredients_file:
			self.ingredients_list.append(normalize_string(line))
		# dedupe the list
		self.ingredients_list = list(set(self.ingredients_list))
		# convert to list items
		ing_list = []
		for line in self.ingredients_list:
			ing_list.append(IngListItem(line, False))
		ingredients_file = open("meats.txt")
		self.ingredients_list = []
		for line in ingredients_file:
			self.ingredients_list.append(normalize_string(line))
		# dedupe the list
		self.ingredients_list = list(set(self.ingredients_list))
		for line in self.ingredients_list:
			ing_list.append(IngListItem(line, True))
		# sort it by length for greedy string matching algorithm
		self.ingredients_list = ing_list
		self.ingredients_list.sort(cmp=comparebylength)
		units_file = open("units.txt")
		for line in units_file:
			self.unit_list.append(IngListItem(normalize_string(line), False))
		self.unit_list = list(set(self.unit_list))
	
	def isIngredient(self, st):
		for s in self.ingredients_list:
			if st == s.name:
				return True
		return False
	
	def isUnit(self, st):
		for s in self.unit_list:
			if st == s.name:
				return True
		return False

	def CreateIngredientFromString(self, st):
		ret = Recipe.Ingredient()
		st = st.lower()
		st = removeParentheticals(st) + " "
		str_toks = st.split(" ")
		try:
			ret.quantity = float(Fraction(str_toks[0]))
			ret.quantity += float(Fraction(str_toks[1]))
		except ValueError:
			pass
		rin = returnFirstMatch(st, self.ingredients_list)
		if rin.name != '':
			ret.name = rin.name
			ret.meat = rin.meat
		
		rin = returnFirstMatch(st, self.unit_list)
		if rin.name != '':
			ret.unit = rin.name
		return ret
