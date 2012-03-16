import TwitterQuery
import pickle
class CandidateSentiment:
    
    def __init__(self):
        #Dictionaries for the naive bayesian filter
        # read python dict back from the file
        
        pkl_file = open('positiveWords.pkl', "rb")
        mydict1 = pickle.load(pkl_file)
        pkl_file.close()
        
        pkl_file = open('negativeWords.pkl', "rb")
        mydict2 = pickle.load(pkl_file)
        pkl_file.close()
        
        #print mydict1
        #print mydict2
        
        self.positiveWords = mydict1[0]
        self.numPositiveSamples = mydict1[1]
        self.negativeWords = mydict2[0]
        self.numNegativeSamples = mydict2[1]
        
        self.candidates = ['Mitt Romney', 'Rick Santorum', 'Newt Gingrich']
        self.trainingSet = ['Greece', 'Abortion', 'Apple']
        
        #Diagnostic
        
        
    def analyzeSentiment(self, tweetCount):
        #First, normalize the positiveWords and negativeWords dictionaries
        check = 0
        for key in self.positiveWords:
            self.positiveWords[key] = float(self.positiveWords[key])/self.numPositiveSamples
            check +=float(self.positiveWords[key])/self.numPositiveSamples
        print check
        
        check = 0
        for key in self.negativeWords:
            self.negativeWords[key] = float(self.negativeWords[key])/self.numNegativeSamples
        print check
        
        print self.positiveWords
        print self.numPositiveSamples
        
        print self.negativeWords
        print self.numNegativeSamples
        
        positiveSentiment = 0
        negativeSentiment = 0
        for candidate in self.candidates:
            bestTweet_pos = "nothing interesting"
            bestTweet_neg = "nothing interesting"
            bestTweet_prating = 0
            bestTweet_nrating = 0
            tweetList = TwitterQuery.search(candidate, results = tweetCount)     
            for tweet in tweetList:
                tweet_sentiment = self.tweetSentiment(tweet)
                if (tweet_sentiment[0]> bestTweet_prating):
                    bestTweet_pos = tweet.content
                if (tweet_sentiment[1] < bestTweet_nrating):
                    bestTweet_neg = tweet.content   
                positiveSentiment += tweet_sentiment[0]
                negativeSentiment += tweet_sentiment[1] 
            print 'The sentiment for ' + candidate + ' is ' + str(positiveSentiment - negativeSentiment)
            print 'The most positive tweet for ' + candidate + ' is ' + '"' + bestTweet_pos + '"'
            print 'The most negative tweet for ' + candidate + ' is ' + '"' +bestTweet_neg + '"'
        
    def tweetSentiment(self, tweet):
        word_list = tweet.content.lower().split()
        p_positiveTweet = self.numPositiveSamples/(self.numNegativeSamples + self.numPositiveSamples)
        p_negativeTweet = 1 - p_positiveTweet
        
        pSum = 0
        nSum = 0
        for word in word_list:
            if(self.positiveWords.has_key(word)):
                pSum += self.positiveWords[word]
            if(self.negativeWords.has_key(word)):
                nSum += self.negativeWords[word]
            
        #Print positive probability and negative probability
        #print ('Positive: ' + str(pSum) + ' Negative: ' + str (nSum) + '\n' + tweet.content + '\n')
        
        return (pSum,nSum)
        
    def train(self):
        for trainer in self.trainingSet:
            #Tweets is a list of dictionaries, where each dictionary is a tweet. The keys are the different parts of the tweet
            tweetList = TwitterQuery.search(trainer, results = 3)
            
            #Dictionary that maps a word to how often it occurs
            wordOccurences = {}      
            for tweet in tweetList:                   
                #Print the tweet, and ask the user to rate if this statement has a positive or negative sentiment        
                tweet.printTweet();
                rated_sentiment = int(raw_input('Tweet Sentiment: -3 to 3: '))
                tweet.content = tweet.content.lower()
                tweet.content = tweet.content.replace(trainer, '')
                word_list = tweet.content.split()
                
                for word in word_list:
                    if(rated_sentiment < 0):
                        if(self.negativeWords.has_key(word)):
                            self.negativeWords[word] = self.negativeWords[word] + abs(rated_sentiment)
                        else:
                            self.negativeWords[word] = abs(rated_sentiment)
                        self.numNegativeSamples = self.numNegativeSamples + abs(rated_sentiment)
                    elif(rated_sentiment > 0):
                        if(self.positiveWords.has_key(word)):
                            self.positiveWords[word] = self.positiveWords[word] + abs(rated_sentiment)
                        else:
                            self.positiveWords[word] = abs(rated_sentiment)
                        self.numPositiveSamples = self.numPositiveSamples + abs(rated_sentiment)
        
        self.writeFiles() 
                 
    def writeFiles(self):
        # write python dict to a file
        write = [self.positiveWords,self.numPositiveSamples]
        output = open('positiveWords.pkl',"wb")
        pickle.dump(write, output)
        output.close()
        
        # write python dict to a file
        write = [self.negativeWords,self.numNegativeSamples]
        output = open('negativeWords.pkl',"wb")
        pickle.dump(write, output)
        output.close()
        
def resetTrainingSet():         
     # write python dict to a file
    write = [{},0]
    output = open('positiveWords.pkl',"wb")
    pickle.dump(write, output)
    output.close()
    
    # write python dict to a file
    output = open('negativeWords.pkl',"wb")
    pickle.dump(write, output)
    output.close()

#resetTrainingSet()                    
c = CandidateSentiment()
choice = raw_input('Train (T) or analyze (A):')

if( choice == 'T'):
    c.train();
else:
    c.analyzeSentiment(50);
    
#c.analyzeSentiment(20)           
        
