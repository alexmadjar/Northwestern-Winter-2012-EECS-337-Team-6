import TwitterQuery
class CandidateSentiment:
    def run(self):
        candidates = ['Mitt Romney', 'Rick Santorum', 'Newt Gingrich']
        for candidate in candidates:
            info = TwitterQuery.search(candidate)
            #Tweets is a list of dictionaries, where each dictionary is a tweet. The keys are the different parts of the tweet
            tweetList = []
            
            #Dictionary that maps a word to how often it occurs
            wordOccurences = {}
            positiveWords = {}
            negativeWords = {}
            for tweet in info:
                t = TwitterQuery.Tweet()
                t.hits = tweet['hits']
                t.author = tweet['trackback_author_nick']
                t.content = tweet['content']
                t.printTweet()
                tweetList.append(t);
            for tweet in tweetList:
                words = tweet.content.lower().split()
                #Add the words to the list
                for word in words:
                    if(wordOccurences.has_key(word)):
                        wordOccurences[word] = wordOccurences[word] + 1
                    else:
                        wordOccurences[word] = 1
                        
            for key in wordOccurences:
                print ("Word: " + key + ' Occurences: ' + str(wordOccurences[key]))
                
 
c = CandidateSentiment()
c.run()           
        