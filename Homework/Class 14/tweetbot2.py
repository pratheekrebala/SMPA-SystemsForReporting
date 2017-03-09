from twython import Twython
import csv

CONSUMER_KEY = '5Fu1ivag6H13k6j9xHK2qUTzu'
CONSUMER_SECRET = 'xnylDZvx2n7ZTlCrWcs7TMhp6eUp2hOlZoAvGQVZotLp6ow6Hf'
ACCESS_TOKEN = '73363519-LnFJ30FsUIIIqh4T1ix3dW8KNBtIbYk977m4fwkfb'
ACCESS_TOKEN_SECRET = 'Cf3deqfcyVxEblklOyp1EMLDMkQutWv6xdHoTHoCGp4tD'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search_term = 'make great again'
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