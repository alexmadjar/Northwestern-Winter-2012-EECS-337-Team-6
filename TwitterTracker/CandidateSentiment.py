import TwitterQuery
class CandidateSentiment:
    
    def __init__(self):
        #Dictionaries for the naive bayesian filter
        self.positiveWords = eval(open("positiveWords.txt").read())[0]
        self.numPositiveWords = eval(open("positiveWords.txt").read())[1]
        self.negativeWords = eval(open("negativeWords.txt").read())[0]
        self.numNegativeWords = eval(open("positiveWords.txt").read())[1]
        
        self.candidates = ['Mitt Romney', 'Rick Santorum', 'Newt Gingrich']
        
    def train(self, tweetCount):
        
        
        
    def train(self):
        for candidate in self.candidates:
            info = TwitterQuery.search(candidate)
            #Tweets is a list of dictionaries, where each dictionary is a tweet. The keys are the different parts of the tweet
            tweetList = []
            
            #Dictionary that maps a word to how often it occurs
            wordOccurences = {}
                       
            for tweet in info:
                t = TwitterQuery.Tweet()
                t.hits = tweet['hits']
                t.author = tweet['trackback_author_nick']
                t.content = tweet['content']
                t.printTweet()
                tweetList.append(t);
                
            for tweet in tweetList:                   
                #Print the tweet, and ask the user to rate if this statement has a positive, negative, or neutral sentiment        
                tweet.printTweet();
                rated_sentiment = float(raw_input('Tweet Sentiment ( -1 to 1: '))
                
                word_list = tweet.content.lower().split()
                
                for word in word_list:
                    #Each word in this tweet is weighted by the rated_sentiment 
                    
                    if(rated_sentiment >= 0):
                        if(self.positiveWords.has_key(word)):
                            self.positiveWords[word] = self.positiveWords[word] + rated_sentiment
                        else:
                            self.positiveWords[word] = rated_sentiment
                        self.numPositiveWords = self.numPositiveWords + 1
                    else:
                        if(self.negativeWords.has_key(word)):
                            self.negativeWords[word] = self.negativeWords[word] + rated_sentiment
                        else:
                            self.negativeWords[word] = rated_sentiment
                        self.numNegativeWords = self.numPositiveWords + 1
                            
                    
                        
                                     
                for key in wordOccurences:
                    
                #print ("Word: " + key + ' Occurences: ' + str(wordOccurences[key]))
            
c = CandidateSentiment()
c.run()           
        