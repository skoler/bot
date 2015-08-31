import praw
r = praw.Reddit(user_agent = 'John Tobin')
subreddit = r.get_subreddit("learnpython")
for submission in subreddit.get_hot(limit = 5):
    print "Title: ", submission.title
    print "Text: ", submission.selftext
    print "Score: ", submission.score
    print "---------------------------------\n"
