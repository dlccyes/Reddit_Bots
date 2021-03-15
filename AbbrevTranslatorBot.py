import praw
import time
import random
import sys

# Enter your correct Reddit information into the variable below
userAgent = 'abbrevtranslatorbot'
cID = 
cSC = 
userN = 'AbbrevTranslatorBot'
userP = 
reddit = praw.Reddit(user_agent=userAgent, client_id=cID,
                     client_secret=cSC, username=userN, password=userP)


subreddit = reddit.subreddit('all')  # any subreddit you want to monitor

cache = []

# bot_message = "  \n\n\n ^^I'm ^made ^by ^[u/yomomaisnotajokebot](https://www.reddit.com/u/yomomaisnotajokebot?utm_medium=android_app&utm_source=share) ^, ^and ^I'm ^not ^like ^the ^other ^bots ^:)     ^DM ^me ^for ^questions ^or ^suggestions" 


def abbrev_translator(comment):
    """detect abbreviations and provide definition'"""
    global cache
    change = False
    abbrev_codomain = {'idk':"I_love Donald_Trump's Kiss"," FYI ":"Fuck You Idiot","LMAO":"Let's Make An Omelette",
    'LOL':'\n- **Lots of Love**\n- **Im severely depressed**\n- **losing over life**\n- **Lucifier our Lord** \n\n ^the ^1st ^provided ^by ^[u/WhyGamingWhy](https://www.reddit.com/user/WhyGamingWhy/) ^, ^the ^2nd ^provided ^by ^[u/Unlimited_Cha0s](https://www.reddit.com/user/Unlimited_Cha0s?utm_medium=android_app&utm_source=share) ^, ^the ^3rd ^provided ^by ^[u/Bobobagginsis](https://www.reddit.com/user/Bobobagginsis/) ^, ^the ^4th ^provided ^by ^[u/Vivit_et_regnat/](https://www.reddit.com/user/Vivit_et_regnat/)',
    'SMH':'Shoot My Head','OMG':"OP's Mom's Gay",'FTFY':'Fuck Them Fuck You','BTW':"Bitch That's Wholesome!",'WTF':"Wow That's Fantastic!",'STFU':'Sorry, Thanks For Understanding',
    'TBH':'To Be Horny','FML':'Fix My Lighthouse',' BS ':"Biden's Sniff  \n\n^provided ^by ^[u/JoshBGaming](https://www.reddit.com/user/JoshBGaming/)"}
    if comment.id not in cache:
        abbrev_translate_meassage = "Hey, I've noticed that you have abbreviations in your comment, some might not know what they mean, so I'll provide a translation for you. \n\n"
        for word in abbrev_codomain:
            if word.lower() in comment.body.lower():
                change = True
                abbrev_translate_meassage += f'{word.strip()} stands for {abbrev_codomain[word]}  \n\n'

        if change == True:
            comment.reply(abbrev_translate_meassage)
            cache.append(comment.id)
            print(abbrev_translate_meassage)

while True:
    for comment in subreddit.comments(limit=10):
        try:
            abbrev_translator(comment)
        except:
            print('blocked i guess')
            time.sleep(70)

            # pass

    if len(cache) > 30:
        del cache[0]

    time.sleep(10)
    # if count > 10:
    # sys.exit()
