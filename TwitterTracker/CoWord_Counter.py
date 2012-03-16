import TwitterQuery

class Word:
    def __init__(self,word):
        self.name = word
        self.CoWords = {}
        self.count = 1
    def printWord(self):
        print '\n' + self.name + ': count= ' + str(self.count) + '\nWords Occurring with this word:'
        for CoWord,num in self.CoWords.iteritems():
            if(num > 1):
                print CoWord + ': ' + str(num)
#
GenericWordsList = ['a','i','or','and','of','by','me','you','this','what','to','my','so','his','he','she','in','the','for','on']
GenericWords = {}
for GenericWord in GenericWordsList:
    GenericWords[GenericWord] = 1
WordOccurrences = {}
for i in range(10):
    TweetList = TwitterQuery.search('santorum',100,i+1)
    tweetcount = 0
    for tweet in TweetList:
    #Filter out non alphanumerics and overly generic words, and strip out connected punctuation
        unfiltered_words = tweet.content.lower().split()
        words = []
        for word in unfiltered_words:
            temp = word.strip('[]{},.<>/?!$%^&*()_-=+|\\;:\'\"')
            if(temp.isalnum() and not GenericWords.has_key(temp)):
                words.append(temp)
    #Delete duplicates
        for word in words:
            for i in range(words.count(word)-1):
                words.remove(word)
    #count occurrences
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
        try:
            word.printWord();
        except:
            pass
    