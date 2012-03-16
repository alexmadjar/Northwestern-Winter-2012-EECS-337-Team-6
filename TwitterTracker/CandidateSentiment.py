import TwitterQuery
import pickle
import time
import datetime
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
        
        self.positiveWords = mydict1
        self.negativeWords = mydict2
        
        
        #self.positiveWords = eval(open('positiveWords2.txt').read())
        #self.negativeWords = eval(open('negativeWords2.txt').read())
        
        
        self.candidates = ['Mitt Romney', 'Rick Santorum', 'Newt Gingrich']
        self.trainingSet = ['Mitt Romney', 'Rick Santorum', 'Newt Gingrich']
        
        #Diagnostic
        
    def analyzeSentimentOverTime(self):
        timeList = []
        for x in range(-10,0):
            time_start = datetime.datetime.now() + datetime.timedelta(days = 10)*x
            time_end = datetime.datetime.now() + datetime.timedelta(days = 10)*(x+1)
            timeList.append( (time_start , time_end) )
        
        for item in timeList:
            t = (time.mktime(item[0].timetuple()),time.mktime(item[1].timetuple()))
            #print ('Time frame: ' + item[0] + ' ' + item[1])
            print 'For time frame starting: ' + str(item[0].month) + ' ' + str(item[0].day) + ' to ' + str(item[1].month) + ' ' + str(item[1].day)
            self.analyzeSentiment(20, time_frame = t)
            print '\n'
        
    def analyzeSentiment(self, tweetCount, time_frame = 0):
        #First, normalize the positiveWords and negativeWords dictionaries
        posCount = 0
        for key in self.positiveWords:
            posCount += self.positiveWords[key]
        negCount = 0
        for key in self.negativeWords:
            negCount += float(self.negativeWords[key])
          
        #Normalize 
          
        for key in self.positiveWords:
            self.positiveWords[key] = float(self.positiveWords[key])/posCount 
        
        for key in self.negativeWords:
            self.negativeWords[key] = float(self.negativeWords[key])/negCount
        
        
        positiveSentiment = 0
        negativeSentiment = 0
        
        candidateSentimentLevels = []
        for candidate in self.candidates:
            if(time_frame == 0):
                tweetList = TwitterQuery.search(candidate, results = tweetCount)
            else:
                tweetList = TwitterQuery.search(candidate, results = tweetCount, mintime = time_frame[0], maxtime = time_frame[1])   

            bestTweet_pos = "nothing interesting"
            bestTweet_neg = "nothing interesting"
            bestTweet_prating = 0
            bestTweet_nrating = 0
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
            print 'The most negative tweet for ' + candidate + ' is ' + '"' + bestTweet_neg + '"'
            candidateSentimentLevels.append(positiveSentiment-negativeSentiment)
            return candidateSentimentLevels

        
    def tweetSentiment(self, tweet):
        word_list = tweet.content.lower().split()
        
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
            tweetList = TwitterQuery.search(trainer, results = 10)
            
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
                    elif(rated_sentiment > 0):
                        if(self.positiveWords.has_key(word)):
                            self.positiveWords[word] = self.positiveWords[word] + abs(rated_sentiment)
                        else:
                            self.positiveWords[word] = abs(rated_sentiment)
        
        self.writeFiles() 
                 
    def writeFiles(self):
        # write python dict to a file
        output = open('positiveWords.pkl',"wb")
        pickle.dump(self.positiveWords, output)
        output.close()
        
        # write python dict to a file
        output = open('negativeWords.pkl',"wb")
        pickle.dump(self.negativeWords, output)
        output.close()
        
def resetTrainingSet():         
     # write python dict to a file
    write = {}
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
    #c.analyzeSentiment(50);
    c.analyzeSentimentOverTime();
    
#c.analyzeSentiment(20)           
        
