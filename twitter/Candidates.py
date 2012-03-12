import Candidate;

def initializeCandidates():
    candict = {'Rick Santorum': ['Santorum'],
               'Ron Paul': ['Ron Paul'],
               'Newt Gingrich': ['Newt'],
               'Mitt Romney': ['Romney']
                }
    candidates = list()
    for name in candict.keys():
        candidates.append(Candidate.makeCandidate(name, candict[name]))
    return candidates

candidates = initializeCandidates()