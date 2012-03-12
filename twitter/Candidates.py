import Candidate;

def initializeCandidates():
    candict = {'Rick Santorum': ['Santorum', '#teamsantorum', '#santorum'],
               'Ron Paul': ['Ron Paul', '#ronpaul2012'],
               'Newt Gingrich': ['Gingrich', '#withnewt'],
               'Mitt Romney': ['Romney', '#mitt2012', '#mittromney']
                }
    candidates = list()
    for name in candict.keys():
        candidates.append(Candidate.makeCandidate(name, candict[name]))
    return candidates

candidates = initializeCandidates()