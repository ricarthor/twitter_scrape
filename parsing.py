import tweepy
import csv
import pandas as pd
import os.path
import argparse

parser = argparse.ArgumentParser(description='Scrape twitter with hash')
parser.add_argument('-nt', '--nr_of_tweets', type=int,  
                    required=True, help='Number of tweets you want')

parser.add_argument('-nf', '--name_of_file', type=str, metavar='', 
                    required=True, help='Check if the file exists')

parser.add_argument('-ht', '--hashtag', type=str, metavar='', 
                    required=True, help='insert the hash you want to scrape')
parser.add_argument('--consumer_key', type=str, metavar='', 
                    required=True, help = 'Consumer key from your Twitter Application Management')
parser.add_argument('--consumer_secret', type=str, metavar='', 
                    required=True, help = 'Consumer Secret from your Twitter Application Management')
parser.add_argument('--access_token', type=str, metavar='', 
                    required=True, help = 'Access token from your Twitter Application Management')
parser.add_argument('--access_token_secret', type=str, metavar='', 
                    required=True, help = 'Access token Secret frmo your Twitter Application Management')
args = parser.parse_args()

def twitter_scrape(nr_tweets, name_of_file, hashtag, consumer_key, consumer_secret, access_token, access_token_secret):
    """
    This functions writes to a csv the tweet's content that have the 
    hashtag that you choose too. The data range is from January 1st. 
    """
    if os.path.isfile(name_of_file):
        raise RuntimeError("File already exists {}".format(name_of_file))

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    # Open/Create a file to append data
    csvFile = open(name_of_file, 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search,q=hashtag,count=100,
                               lang="en",
                               since='2017-01-01').items(nr_tweets):
        csvWriter.writerow([tweet.text.encode('utf-8')])
    print ('You scraped it well')
    
if __name__ == '__main__':
    twitter_scrape(args.nr_of_tweets, 
                   args.name_of_file, 
                   args.hashtag, 
                   args.consumer_key, 
                   args.consumer_secret, 
                   args.access_token, 
                   args.access_token_secret)
