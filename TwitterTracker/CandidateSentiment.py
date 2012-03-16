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
        
        print mydict1
        print mydict2
        
        self.positiveWords = mydict1[0]
        self.numPositiveSamples = mydict1[1]
        self.negativeWords = mydict2[0]
        self.numNegativeSamples = mydict2[1]
        
        self.candidates = ['Mitt Romney', 'Rick Santorum', 'Newt Gingrich']
        
        #Diagnostic
        
        
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
        p_positiveTweet = self.numPositiveSamples/(self.numNegativeSamples + self.numPositiveSamples)
        p_negativeTweet = 1 - p_positiveTweet
        
        # p_positiveGivenWord = (%positive samples) * (p_WordgivenPositive)
        
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
            #Tweets is a list of dictionaries, where each dictionary is a tweet. The keys are the different parts of the tweet
            tweetList = TwitterQuery.search(candidate)
            
            #Dictionary that maps a word to how often it occurs
            wordOccurences = {}      
            for tweet in tweetList:                   
                #Print the tweet, and ask the user to rate if this statement has a positive or negative sentiment        
                tweet.printTweet();
                rated_sentiment = raw_input('Tweet Sentiment: P or N')
                
                word_list = tweet.content.lower().split()
                
                for word in word_list:
                    
                    if(rated_sentiment == 'P'):
                        if(self.positiveWords.has_key(word)):
                            self.positiveWords[word] = self.positiveWords[word] + 1
                        else:
                            self.positiveWords[word] = 1
                        self.numPositiveSamples = self.numPositiveSamples + 1
                    else:
                        if(self.negativeWords.has_key(word)):
                            self.negativeWords[word] = self.negativeWords[word] + 1
                        else:
                            self.negativeWords[word] = 1
                        self.numNegativeSamples = self.numNegativeSamples + 1
        
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

      
 # write python dict to a file
write = [{},0]
output = open('positiveWords.pkl',"wb")
pickle.dump(write, output)
output.close()

# write python dict to a file
output = open('negativeWords.pkl',"wb")
pickle.dump(write, output)
output.close()
                    
c = CandidateSentiment()
choice = raw_input('Train (T) or analyze (A):')

if( choice == 'T'):
    c.train();
else:
    c.analyze(20);
    
#c.analyzeSentiment(20)           
        