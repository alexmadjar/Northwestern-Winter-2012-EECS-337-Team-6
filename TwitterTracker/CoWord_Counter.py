import TwitterQuery

class Word:
    def __init__(self,word):
        self.name = word
        self.CoWords = {}
        self.count = 1
    def printWord(self):
        print '\n' + self.name + ': count= ' + str(self.count) + '\nWords Occurring with this word:'
        for CoWord,num in self.CoWords.iteritems():
            if(num/self.count > .50):
                print CoWord + ': ' + str(num)
#
    
WordOccurrences = {}

TweetList = TwitterQuery.search('santorum',100)

for tweet in TweetList:
    words = tweet.content.lower().split()
    for word in words:
        if(WordOccurrences.has_key(word)):
            WordOccurrences[word].count += 1
            CurrentWord = WordOccurrences[word]
        else:
            CurrentWord = Word(word)
            WordOccurrences[word] = CurrentWord
        for OtherWord in words:
            if(OtherWord != CurrentWord.name):
                if(CurrentWord.CoWords.has_key(OtherWord)):
                    CurrentWord.CoWords[OtherWord] += 1
                else:
                    CurrentWord.CoWords[OtherWord] = 1
#
for label,word in WordOccurrences.iteritems():
    if(word.count > 5):
        word.printWord();