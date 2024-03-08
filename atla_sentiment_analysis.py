import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd 
import tokens

# set up credentials
consumer_key = tokens.consumer_key
consumer_secret = tokens.consumer_secret
access_token = tokens.access_token
access_token_secret = tokens.access_token_secret
bearer_token = tokens.bearer_token

# authenticate woth Twitter API 
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

client = tweepy.Client(
    # bearer_token = bearer_token,
    consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    access_token = access_token,
    access_token_secret = access_token_secret
)

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

def get_tweets(client, query, count):
    tweets = []
    try:
        fetched_tweets = client.search_recent_tweets(query=query)
        for tweet in fetched_tweets.data:
            # tweets.append(tweet.text)
            print(tweet.text)
        return tweets
    except Exception as e:
        print("Error in get_tweets: ", e)
        return []

def main():
    # Get tweets for a specific query (e.g., a hashtag or keyword)
    query = "#AvatarNetflix"  
    tweets = get_tweets(client, query, 100)

    # Analyze sentiment for each tweet
    sentiments = [analyze_sentiment(tweet) for tweet in tweets]

    # Create a DataFrame to store the data
    data = pd.DataFrame({"Tweet": tweets, "Sentiment": sentiments})

    # Plot sentiment distribution
    plt.hist(sentiments, bins=[-1, -0.5, 0, 0.5, 1], color='lightblue', edgecolor='black')
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.title('Sentiment Analysis of Tweets')
    plt.show()

    # Display the analyzed data
    print(data.head(10))

if __name__ == "__main__":
    main()

