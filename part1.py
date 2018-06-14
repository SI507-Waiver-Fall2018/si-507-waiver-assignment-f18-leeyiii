# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>
name = sys.argv[1]
tweetCount = sys.argv[2]

#secret data
consumer_key="Fe8SgOwx3kLZdKBkheaXsUI17"
consumer_secret="Ypl7Tlf3HJHvaipbJE7oyB8afG0WIixXRVxDqviMXvVwUqns4Z"
access_token="4858990592-0HfFBiXrZZtUg6AWLvVOcrprkUIErJ4F28rAnIL"
access_token_secret="Bik4x8ctRYvY5rGgSTeGYbVyc7IHs9OQ5CKiHjsOpKTvs"

#data request
auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#request data 
def request(name, tweetCount):
	results = api.user_timeline(id=name, count=tweetCount, tweet_mode="extended")
	return results

#get tweets
tweet_lists=[]
for tweet in request(name, tweetCount):
	tweet_lists.append(tweet.full_text)



##Analyze Tweets

real_words_lst = [] # create a list to store content:
ignore_lst = ["http", "https", "RT"] # create a list of words that should be ignored


from nltk.tokenize import word_tokenize

## go through each tweet & add real words to real_words_lst
for tweet in tweet_lists:
    tokenized_text = word_tokenize(tweet) # tokenize the words in the tweet

    # iterate through each word in tokenized_text & filter out the word if it's a stop word
    for word in tokenized_text:
        # check if the word starts with an alphabetic character [a-zA-Z]
        # check if the word is not in the ignore_lst
        if word[0].isalpha() and word not in ignore_lst:
            real_words_lst.append(word) # add the word to real_words_lst
        #else:
            #print("Not a word: " + str(word))
            #continue

print(real_words_lst)

## calcuate frequency distribution on real words
real_words_dic = nltk.FreqDist(real_words_lst)

## sort the words by their frequency
sorted_real_words_freq = sorted(real_words_dic.items(), key = lambda x: x[1], reverse = True)

## print the 5 most common words
print("THE 5 MOST FREQUENTLY USED WORDS:")
for word_freq_tuple in sorted_real_words_freq[0:5]:
    word, frequency = word_freq_tuple # unpack the tuple
    print(word, ":", frequency, "times")












