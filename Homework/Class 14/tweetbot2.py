from twython import Twython
import csv

CONSUMER_KEY = 'welp'
CONSUMER_SECRET = 'welp'
ACCESS_TOKEN = 'welp'
ACCESS_TOKEN_SECRET = 'welp'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search_term = 'make -america great again'
search = twitter.search(q=search_term, count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[[search_term, result['text'].encode('utf-8'), url]]
        a.writerows((text))