import praw
import time

f = open("D://Github Details//basic-reddit-bot_details.txt","r")
lines = f.readlines()

reddit = praw.Reddit(client_id = "{}".format((lines[0]).strip()),
                     client_secret = "{}".format((lines[1]).strip()),
                     username = "{}".format((lines[2]).strip()),
                     password = "{}".format((lines[3]).strip()),
                     user_agent = "{}".format((lines[4]).strip()))

