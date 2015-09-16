from twython import Twython, TwythonError

# Requires Authentication as of Twitter API v1.1
twitter = Twython('ffTvOIZqqWn9japC6mJ8n02Mc', 'L9lYgDMUfXi2Ev6iVSmukGOJlkdMobOR0UToFNDKlai81RnE5W', '499163854-N4BesXw2V5wFwH2vnTChqwtSmdRP2MY9JqXXXhUB', 'oNNox40GznN1hMY1TDGJLTojUObY9B30993uAogUFWd6c')
try:
    search_results = twitter.search(q='Climate Change', count=50)
except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
