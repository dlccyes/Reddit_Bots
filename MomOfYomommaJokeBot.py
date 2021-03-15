import praw
import time
import random
import sys
import datetime


userAgent = 'MomOfYoMommaJokeBot'
cID = 
cSC = 
userN = 'MomOfYoMommaJokeBot'
userP = 

reddit = praw.Reddit(user_agent=userAgent, client_id=cID,
                     client_secret=cSC, username=userN, password=userP)

yomoma_replies = ["My son is very wholesome, stop spamming RIGHT NOW!!!!",
"please do not stop my sweet son from praising other's mom will you",
"My son is very wholesome, and so do I, please do not insult us.",
"fuck fuck fuck fuck stop hurtin my son!!!!!!!!",
"Why do you want to fuck me? Stop harassing me and my son!!!!",
"Your daddy is so retard that he had someone like you.",
"shut the fuck up or I'll fuck your fucking retard dada",
'Yo dada is so fat that ur beautiful latinx mama cannot even breathe when trying to create you'
]

YoMomma_replies = ["You're doing good, my son.",
"Do not be affected by that retard called yomomaisnotajokebot son, it's just a dumb bot.",
"That's wholesome!!! I'm so proud of you!!",
"You're the best bot in the world, my son.",
'good bot']

count = 0
cache = []
bot_message = "  \n\n\n^I ^am ^YoMommaJokeBot's ^mommy. ^Downvote ^will ^not ^remove. ^Upvote ^to ^fuck ^yomommaisnotajokebot."

def reply(redditor,replies):
    global bot_message, cache
    comment = redditor.comments.new(limit=10)
    for cc in comment:
        if cc.id not in cache:
            deltat = datetime.datetime.now() - datetime.datetime.fromtimestamp(cc.created_utc)
            if int(str(deltat).split(':')[1]) <= 2:
                random.shuffle(replies)
                cc.reply(replies[0]+bot_message)
                print('success')
                cache.append(cc.id)

            else:
                print('no rn')
                pass

    
redditor_YoMomma = reddit.redditor('YoMommaJokeBot')
redditor_yomoma = reddit.redditor('yomomaisnotajokebot')

while True:
    try:
        if random.randint(0,2)==1:
            reply(redditor_YoMomma,YoMomma_replies)
        else:
            reply(redditor_yomoma,yomoma_replies)        

        if len(cache) > 30:
            del cache[0]
        time.sleep(70)

    except:
        print('blocked')
        time.sleep(180)
