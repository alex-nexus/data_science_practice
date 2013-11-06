from pattern.web import Twitter, plaintext
for tweet in Twitter().search('"more important than"', cached=False):
	print plaintext(tweet.description)
