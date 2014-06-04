get_twitter_followers.py

example GET request url: https://api.twitter.com/1.1/users/lookup.json?screen_name=twitterapi,twitter

url = "https://api.twitter.com/1.1/users/lookup.json?screen_name=%%"

ids = al_ents['twi_url']

for id in ids:
	url = _BASE_URL.replace('%%', id)