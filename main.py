# BoneAppleTeaBot 6816
# By Marcell Laszlo Meszaros
# Started on the 22/11/2019
# Version: 1.0
# Github Link: https://github.com/marmesz/BoneAppleTeaBot-6816
# Facebook Link: https://www.facebook.com/batbot6816


# Imports
import praw
import facebook
import urllib.request

import tokens  # Credentials file


# Settings
TESTING_MODE = False


# Authorization Tokens
reddit = praw.Reddit(client_id=tokens.r_token[0],  # Refers to an external file that contains all credentials.
                     client_secret=tokens.r_token[1],  # You can just use your normal reddit OAuth credentials here.
                     user_agent=tokens.r_token[2],
                     username=tokens.r_token[3],
                     password=tokens.r_token[4])

graph = facebook.GraphAPI(access_token=tokens.f_token, version="2.12")


# Reddit Settings
subreddit = reddit.subreddit('BoneAppleTea')
post = subreddit.random()

# Downloads image from reddit post (Graph API can't use link as target..)
urllib.request.urlretrieve(post.url, 'post_image.png')

# Generates text output
output_text = "Title: {}\nAuthor: {}\nScore: {}\nLink: {}".format(post.title, post.author, post.score, post.url)

# Facebook Upload Sequence
if TESTING_MODE:
    print(output_text)
else:
    try:
        main_post = graph.put_photo(image=open('post_image.png', 'rb'), message=output_text)  # Uploads main post
        graph.put_comment(main_post['id'], message="Like this bot? Why not check out the Github?\n"
                                                   "https://github.com/marmesz/BoneAppleTeaBot-6816")
    except:
        main_post = graph.put_photo(image=open('post_image.png', 'rb'), message=output_text)  # Uploads main post
        graph.put_comment(main_post['id'], message="Like this bot? Why not check out the Github?\n"
                                                   "https://github.com/marmesz/BoneAppleTeaBot-6816")
    print("Post successful!")

