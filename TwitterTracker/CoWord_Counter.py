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
query = 'santorum'
GenericWordsList = ['a', 'about', 'after', 'all', 'and', 'any', 'an', 'are', 'as', 'at', 'been', 'before', 
  'be', 'but', 'by', 'can', 'could', 'did', 'down', 'do', 'first', 'for', 'from', 'good', 'great', 'had', 
  'has', 'have', 'her', 'he', 'him', 'his', 'if', 'into', 'in', 'is', 'its', 'it', 'I', 'know', 'like', 
  'little', 'made', 'man', 'may', 'men', 'me', 'more', 'Mr', 'much', 'must', 'my', 'not', 'now', 'no', 'of', 
  'on', 'one', 'only', 'or', 'other', 'our', 'out', 'over', 'said', 'see', 'she', 'should', 'some', 'so', 
  'such', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'time', 'to', 
  'two', 'upon', 'up', 'us', 'very', 'was', 'were', 'we', 'what', 'when', 'which', 'who', 'will', 'with', 
  'would', 'you', 'your']
GenericWords = {}
for GenericWord in GenericWordsList:
    GenericWords[GenericWord] = 1
WordOccurrences = {}
for i in range(10):
    TweetList = TwitterQuery.search(query,100,i+1)
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
        important_words = []
        has_word = False
        for co_word,co_count in word.CoWords.iteritems():
            if (co_count/word.count > .5):
                has_word = True
                important_words.append(co_word)
        if(has_word):
            important_words.append(word.name)
            print '\n\n\nTrend found, words are: '
            for trend_word in important_words:
                print trend_word
            new_query = query
            for imp_word in important_words:
                new_query += ' '
                new_query += imp_word
            TweetList = TwitterQuery.search(new_query,10,1)
            print '\nSome representative tweets:'
            for tweet in TweetList:
                try:
                    print tweet.content
                except:
                    print 'failed to print tweet'