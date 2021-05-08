import praw
import time

f = open("D://Github Details//basic-reddit-bot_details.txt","r")
lines = f.readlines()

reddit = praw.Reddit(client_id = "{}".format((lines[0]).strip()),
                     client_secret = "{}".format((lines[1]).strip()),
                     username = "{}".format((lines[2]).strip()),
                     password = "{}".format((lines[3]).strip()),
                     user_agent = "{}".format((lines[4]).strip()))

def spamcheck(kw):
    authorl = []
    for submission in reddit.subreddit("all").search(kw, sort = "new", limit = 20):
        print("\n\nTITLE: ", submission.title,
              "\n\tAUTHOR: ", submission.author,
              "\n\t LINK: ", submission.url)
        if submission.author not in authorl:
            authorl.append(submission.author)
    return authorl

if __name__ == "__main__":
    authors = spamcheck("Free Udemy")
    for author in authors:
        print(author)