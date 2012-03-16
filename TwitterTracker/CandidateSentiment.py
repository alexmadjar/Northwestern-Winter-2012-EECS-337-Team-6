import TwitterQuery
class CandidateSentiment:
    
    def __init__(self):
        #Dictionaries for the naive bayesian filter
        self.positiveWords = eval(open("positiveWords.txt").read())[0]
        self.numPositiveSamples = eval(open("positiveWords.txt").read())[1]
        self.negativeWords = eval(open("negativeWords.txt").read())[0]
        self.numNegativeSamples = eval(open("positiveWords.txt").read())[1]
        
        self.candidates = ['Mitt Romney', 'Rick Santorum', 'Newt Gingrich']
        
    def analyzeSentiment(self, tweetCount):
        #First, normalize the positiveWords and negativeWords dictionaries
        for key in self.positiveWords:
            self.positiveWords[key] = self.positiveWords[key]/self.numPositiveSamples
        
        for key in self.negativeWords:
            self.negativeWords[key] = self.negativeWords[key]/self.numNegativeSamples
        
        #Run Naive Bayes Filter on many tweets
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
                self.tweetSentiment(tweet) 
        
    def tweetSentiment(self, tweet):
        word_list = tweet.content.lower().split()
        p_positiveTweet = self.numPositiveSamples/self.numNegativeSamples
        p_negativeTweet = 1 - p_positiveTweet
        
        p_positiveGivenWord = p_positiveTweet
        p_negativeGivenWord = p_negativeTweet
        for word in word_list: 
            p_wordGivenPositive = self.positiveWords[word]
            p_wordGivenNegative = self.negativeWords[word]
            
            p_positiveGivenWord = p_positiveGivenWord * p_wordGivenNegative
            p_negativeGivenWord = p_negativeGivenWord * p_wordGivenPositive
            
            
        #Print positive probability and negative probability
        print ('Positive: ' + str(p_positiveGivenWord) + ' Negative: ' + str (p_negativeGivenWord) + '\n' + tweet.content)
        
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
                #Print the tweet, and ask the user to rate if this statement has a positive or negative sentiment        
                tweet.printTweet();
                rated_sentiment = float(raw_input('Tweet Sentiment: P or N'))
                
                word_list = tweet.content.lower().split()
                
                for word in word_list:
                    
                    if(rated_sentiment == 'P'):
                        if(self.positiveWords.has_key(word)):
                            self.positiveWords[word] = self.positiveWords[word] + 1
                        else:
                            self.positiveWords[word] = rated_sentiment
                        self.numPositiveSamples = self.numPositiveSamples + 1
                    else:
                        if(self.negativeWords.has_key(word)):
                            self.negativeWords[word] = self.negativeWords[word] + 1
                        else:
                            self.negativeWords[word] = rated_sentiment
                        self.numNegativeSamples = self.numNegativeSamples + 1
            
c = CandidateSentiment()
c.run()           
        