

#FULL NAME: Yi Lee
#UMICH UNIQUENAME: yilee


# these should be the only imports you need
import tweepy
import nltk
import json
import sys

#--Part1 request twitter data--

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



def request(name, tweetCount):
	results = api.user_timeline(id=name, count=tweetCount, tweet_mode="extended")
	return results



#get tweets
tweet_lists=[]
for tweet in request(name, tweetCount):
	tweet_lists.append(tweet.full_text)



print ("USER:" , name)
print ("TWEETS ANALYZED:" , tweetCount)

#--Part2 Analyze Tweets--


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



tag_lst=nltk.pos_tag(real_words_lst)

#--Part2.1 Five most frequent verbs--

vb_lst=[]

for word_tag_tuple in tag_lst:
    if word_tag_tuple[1][:2] == 'VB':
        vb_lst.append(word_tag_tuple[0])

## calcuate frequency distribution on real words
vb_freq_dic = nltk.FreqDist(vb_lst)



## sort the words by their frequency
sorted_vb_freq_lst = sorted(vb_freq_dic.items(), key = lambda x: x[1], reverse = True)


## print the 5 most common words
print("VERBS:", end=' ')
for word_freq_tuple in sorted_vb_freq_lst[0:5]:
    word, frequency = word_freq_tuple # unpack the tuple
    print(word,  "(" + str(frequency) + ")"  , end=' ')
print('')

#--Part2.2 Five most frequent nouns--

nn_lst=[]

for word_tag_tuple in tag_lst:
    if word_tag_tuple[1][:2] == 'NN':
        nn_lst.append(word_tag_tuple[0])

## calcuate frequency distribution on real words
nn_freq_dic = nltk.FreqDist(nn_lst)



## sort the words by their frequency
sorted_nn_freq_lst = sorted(nn_freq_dic.items(), key = lambda x: x[1], reverse = True)


## print the 5 most common words
print("NOUNS:", end=' ')
for word_freq_tuple in sorted_nn_freq_lst[0:5]:
    word, frequency = word_freq_tuple # unpack the tuple
    print(word,  "(" + str(frequency) + ")" , end=' ')
print('')
#--Part2.3 Five most frequent adjectives--

ad_lst=[]

for word_tag_tuple in tag_lst:
    if word_tag_tuple[1][:2] == 'JJ':
        ad_lst.append(word_tag_tuple[0])

## calcuate frequency distribution on real words
ad_freq_dic = nltk.FreqDist(ad_lst)



## sort the words by their frequency
sorted_ad_freq_lst = sorted(ad_freq_dic.items(), key = lambda x: x[1], reverse = True)


## print the 5 most common words
print("ADJECTIVES:", end=' ')
for word_freq_tuple in sorted_ad_freq_lst[0:5]:
    word, frequency = word_freq_tuple # unpack the tuple
    print(word,  "(" + str(frequency) + ")" , end=' ')
print('')


#--Part2.4 get the number of original tweets, favorites, and retweets--

#count original tweets
ori_tweets=0
ori_tweets_lists=[]
ori_tweets_status=[]
for tweet in request(name, tweetCount):
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
        ori_tweets += 1
        ori_tweets_status.append(tweet)
        ori_tweets_lists.append(tweet.full_text)


ori_fav_count=0
for tweet in ori_tweets_status:
    #print(tweet.favorite_count)
    ori_fav_count=ori_fav_count+tweet.favorite_count
    

ori_re_count=0
for tweet in ori_tweets_status:
    #print(tweet.retweet_count)
    ori_re_count=ori_re_count+tweet.retweet_count



## print the number of original tweets

print("ORIGINAL TWEETS:", ori_tweets)

## print the number of favorites
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY):",ori_fav_count)

## print the number of retweets
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY):", ori_re_count)


## made a CSV file of the 5 most frequent nouns 

f = open("noun_data.csv","w")
f.write("Noun, Number\n")

for word_freq_tuple in sorted_nn_freq_lst[0:5]:
    word, frequency = word_freq_tuple
    f.write("{},{}\n".format(word, str(frequency)))
f.close()









