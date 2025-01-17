max_chars = 140
tweet = input('enter your tweet: ')

length = len(tweet)

if length < max_chars:
    print(f"That {length} character tweet will work!")
else:
    print(f"That {length} character tweet is {length - max_chars} characters too long!")