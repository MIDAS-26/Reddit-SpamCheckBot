import praw
import time
import random
import keyboard

f = open("D://Github Details//basic-reddit-bot_details.txt","r")
lines = f.readlines()

reddit = praw.Reddit(client_id = "{}".format((lines[0]).strip()),
                     client_secret = "{}".format((lines[1]).strip()),
                     username = "{}".format((lines[2]).strip()),
                     password = "{}".format((lines[3]).strip()),
                     user_agent = "{}".format((lines[4]).strip()))

spamwords = ["free udemy", "free course", "discount", "coupon", "free", "save"]


def spamcheck(kw):
    authorl = []
    for submission in reddit.subreddit("all").search(kw, sort = "new", limit = 10):
        if submission.author not in authorl:
            authorl.append(submission.author)
    return authorl

if __name__ == "__main__":
    while True:
        keyword = random.choice(["free udemy", "free course"])
        sus_authors = spamcheck(keyword)
        spam_authors = {}
        spam_details = []
        spam_scorel = []


        for author in sus_authors:
            spam_links = []
            post_total = 0
            post_spam = 0
            try:
                for post in reddit.redditor(str(author)).submissions.new():
                    post_link = post.url
                    post_subreddit = post.subreddit
                    post_title = post.title
                    post_id = post.id
                    spam = False
                    for kw in spamwords:
                        if kw in post.title.lower():
                            spam = True
                            junk = [post_id, post_title, str(author)]
                            if junk not in spam_links:
                                spam_links.append(junk)
                    if spam:
                        post_spam += 1
                    post_total += 1           
                try:
                    spam_score = round((post_spam/post_total), 3)
                except:
                    spam_score = 0
                

                if spam_score>=0.3:
                    if str(author) not in spam_scorel:
                        print("{}'s Spam Score is: {}".format(author, spam_score))
                        spam_authors[str(author)] = [spam_score, post_total]
                        spam_scorel.append(str(author))
                        for links in spam_links:
                            spam_details.append(links)
                    
            except:
                print(author)
                    







    