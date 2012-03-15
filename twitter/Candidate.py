def makeCandidate(name, keywords):
	ret = Candidate();
	ret.keywords = keywords;
	ret.name = name;
	return ret;

class Candidate:
    def __init__(self):
    	keywords = [];
    	name = '';
    