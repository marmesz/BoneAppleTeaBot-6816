**Welcome to BoneAppleTea Bot's Github!** 

This bot takes a randomly chosen image from r/BoneAppleTea, and posts it on Facebook every two hours.
As you can tell by the source code, it is a very simple bot for the time being.
However, I have many other features in mind which I will implement very soon.

Feel free to use the source code of this bot for other projects - I tried my best to commentate the source code as much 
as possible. 

Behind the scenes, this bot uses the PRAW wrapper, as well as the facebook-sdk.
The `tokens.py` file which is referred to in the code, contains the information used by PRAW and facebook-sdk:
- r_token - a list, which contains each element of the OAuth2 system for reddit
- f_token - a string, that stores a permanent Facebook token used by the SDK


If you have any questions at all, feel free to contact me at marcell.mesz@gmail.com.
