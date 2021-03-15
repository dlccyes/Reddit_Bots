import praw
import time
import random
import sys
import datetime


userAgent = 'yomomaisnotajokebot'
cID = 
cSC = 
userN = 'yomomaisnotajokebot'
userP = 

reddit = praw.Reddit(user_agent=userAgent, client_id=cID,
                     client_secret=cSC, username=userN, password=userP)

replies = ["his (or her) mama is a nice person, but YoMommaJokeBot's mama is a total joke",
           "YoMommaJokeBot's mama is a disgrace for having such a son just randomly joking about others' mom",
           "yo mama fat",
           "YoMommaJokeBot's mama is so fat that ISS astronaut can see her from space",
           "YoMommaJokeBot's mama is a total joke",
           "joking about others' beautiful mother is not wholesome",
           "my momma is very nice, and so is his (or her) mum, but YoMommaJokeBot's mammmmmaaaa is the fatest latinx womxn I've ever seen",
           "my mama is a beautiful latinx womxn, but YoMommaJokeBot's muuuum is not",
           "Do you know why joe mama is so funny? Because yo(MommaJokeBot's) mammmmma is a total joke :))",
           "YoMommaJokeBot is such a loser that it can only joke about others' beautiful intelligent independent latinx mama to gain some dignity, but ppl just won't respect a person who doesn't respect the most important element in our society: the beautiful mamas :)).",
           "YoMommaJokeBot should be permantly banned for disrepecting the wonderful latinx womxn not only living in my home but also inside everyone's heart: my mama",
           "my mama is the best, OP's mum is pretty decent too, but YoMommaJokeBot's MAMMA is just so fat",
           "rains are actually from YoMommaJokeBot's fat ass mama's sweat, becuz she's so fat",
           "Scientists from multiple countries have already formed an international research team, dedicated to find out why YoMommaJokeBot's mother is so fat.",
           "Yomamma so fat that they had to extend the dictionary just to define how fat she is. Also the yomamma jokes are old man or woman  \n\n^(an ^actual ^comment ^from ^[u/underagesenpai](https://www.reddit.com/user/underagesenpai/))",
           "Yo mama so chaotic she make Tyra Banks look mostly normal  \n\n^(an ^actual ^comment ^from ^[u/alannacoke](https://www.reddit.com/user/alannacoke/))",
           "Yo mama so chaotic she makes C17 look high fashion  \n\n^(an ^actual ^comment ^from ^[u/TheBrilliantaReality](https://www.reddit.com/user/TheBrilliantaReality/))"]
count = 0
cache = []
bot_message = "  \n\n\n^I ^am ^a ^bot ^that ^fucks ^YoMommaJokeBot's ^mum. ^Downvote ^will ^not ^remove. ^Upvote ^to ^fuck ^this ^bot."

while True:
    try:
        redditor = reddit.redditor('YoMommaJokeBot')
        comment = redditor.comments.new(limit=10)

        for cc in comment:
            if cc.id not in cache:
                deltat = datetime.datetime.now() - datetime.datetime.fromtimestamp(cc.created_utc)
                if int(str(deltat).split(':')[1]) <= 2:

                    a = random.randint(0, 2)
                    if a == 0:  # 1/3 chance
                        cclist = cc.body.split(' ')
                        as1 = cclist.index('as')
                        cclist = cclist[as1+1:]
                        as2 = cclist.index('as')
                        cclist = cclist[0:as2]
                        ccstr = ''
                        for i in range(len(cclist)):
                            ccstr += cclist[i] + ' '
                        cc.reply(f'You are so dumb, yo mom is clearly more {ccstr}'+bot_message)
                        print('success')
                        cache.append(cc.id)

                    else:
                        random.shuffle(replies)
                        cc.reply(replies[0]+bot_message)
                        print('success')
                        cache.append(cc.id)
                        count += 1

                else:
                    print('no rn')
                    pass

        if len(cache) > 30:
            del cache[0]
        time.sleep(70)
        # if count > 20:
        # sys.exit()

    except:
        print('blocked')
        time.sleep(180)
