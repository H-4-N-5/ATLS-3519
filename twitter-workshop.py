#!/usr/bin/env python

from twython import Twython

APP_KEY = 'ffTvOIZqqWn9japC6mJ8n02Mc'
APP_SECRET = 'L9lYgDMUfXi2Ev6iVSmukGOJlkdMobOR0UToFNDKlai81RnE5W'

OAUTH_TOKEN = '499163854-N4BesXw2V5wFwH2vnTChqwtSmdRP2MY9JqXXXhUB'
OAUTH_TOKEN_SECRET = 'oNNox40GznN1hMY1TDGJLTojUObY9B30993uAogUFWd6c'


twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)



twitter.search(q='twitter', result_type='popular')
