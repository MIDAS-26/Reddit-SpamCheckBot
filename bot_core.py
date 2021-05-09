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

spamwords = ["free cryptocurrency", "free crypto", "you send", "we send double", "free", "free money", "giveaway crypto", "get double crypto", "free cash", "free bitcoin"]
spam_warnu = []
spam_warnid = []


def spamcheck(kw):
    authorl = []
    for submission in reddit.subreddit("all").search(kw, sort = "new", limit = 30):
        if submission.author not in authorl:
            authorl.append(submission.author)
    return authorl

if __name__ == "__main__":
    while True:
        keyword = random.choice(["free crypto", "get double crypto", "free cash", "free bitcoin", "referral", "free money"])
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
                

                if spam_score>=0.4:
                    if str(author) not in spam_scorel:
                        print("{}'s Spam Score is: {}".format(author, spam_score))
                        spam_authors[str(author)] = [spam_score, post_total]
                        spam_scorel.append((str(author), spam_score))
                        for links in spam_links:
                            spam_details.append(links)
                        
                    
            except Exception as e:
                print("From", author, e)
                

        for i in range(len(spam_details)):
            if spam_details[i][2] not in spam_warnu:
                spam_warnu.append(spam_details[i][2])
                spam_warnid.append(spam_details[i][0])
                
            submission = reddit.submission(id = spam_details[i][0])
            link = "https://reddit.com"+submission.permalink
            message = """*Beep Bop*
            \nI am a bot that sniffs out spammers, this smells like SPAM.
            \nMost submissions from /u/{} appear to be SPAM.
            \nIf someone tells you to send crypto to a wallet link and they will send back double, DON'T SEND ANY CRYPTO.
            \nMay the Force be with you.
            \n*Beep Bop*""".format(spam_details[i][2])  
            try:
                with open("posted_urls.txt","r") as f:
                    already_posted = f.read().split("\n")
                if link not in already_posted:
                    print(message)
                    submission.reply(message)
                    print("Posted to {}, now sleeping for 12 minutes.".format(link))
                    with open("posted_urls.txt", "a") as f:
                        f.write(link+"\n")
                    time.sleep(12*60)
                    break
            except Exception as e:
                print(e)
                time.sleep(12*60)

    
