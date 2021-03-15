import praw
import time
import random
import sys

# Enter your correct Reddit information into the variable below

userAgent = 'verywholesomebot'
cID = 
cSC = 
userN = 'Very_Wholesome_Bot'
userP = 
reddit = praw.Reddit(user_agent=userAgent, client_id=cID,
                     client_secret=cSC, username=userN, password=userP)


subreddit = reddit.subreddit('all')  # any subreddit you want to monitor

cache = []

bot_message = "  \n\n\n ^^I'm ^made ^by ^[u/yomomaisnotajokebot](https://www.reddit.com/u/yomomaisnotajokebot?utm_medium=android_app&utm_source=share) ^, ^and ^I'm ^not ^like ^the ^other ^bots ^:)     ^DM ^me ^for ^questions ^or ^suggestions"


def wholesome_spam(comment):
    """detect unwholesome score and spam wholesome message"""
    global count, cache, bot_message
    badwords = [' hate', 'fuck', 'bitch', 'punch', ' kill', 'murder', 'negative', ' pathetic', 'dirty', 'shit', 'retard', 'dumb',
                'death', 'threat', ' lie', 'damn', 'scam', 'spam', 'cock', 'hell', 'worse', ' ass ', 'asshole', 'stupid', 'idiot', 'racist', 'dick']
    badwords_count = 0
    if comment.id not in cache:
        for word in badwords:  # goes through our keywords
            if word in comment.body.lower():
                # badwords_count += 1
                badwords_count += comment.body.lower().count(word)
        if badwords_count > 1:
            badwords_message = f"Hey, I've noticed that you have at least {badwords_count} bad words in your comment :(  \n\nHere's what you should say instead:  \n\n---#########---  \n\nI love you 🤗🤗🤗 You're so cute that I almost want to eat you 🤤🤤  \n\n---#########---  \n\nPlease try it next time, remember, keep it wholesome :))"
            comment.reply(badwords_message+bot_message)
            cache.append(comment.id)
            print(badwords_message)
        # else:
            # print('nope')


def wholesome_conversion(comment):
    """convert bad words to wholesome words"""
    global count, cache, bot_message
    change = False
    wholesome_codomain = {'no bad': '**super wholesome**', 'not bad': '**super wholesome :)**', ' hate': ' **love**', 'fucking': '**wholesome**', 'fuck': '**cute duck**', 'bad': '**good**', 'bitch': '**cute dog**',
                          ' hot ': ' **comfortable** ', ' cold ': ' **comfortable** ', 'punch': '**hug**', 'suicide': '**realize how beautiful the world is**', 'Ronaldo': '**mesi**',
                          'pathetic': '**wonderful**', 'negative': '**very positive :))**', 'dirty': '**clean**', 'shit': '**delicious cake**',
                          ' kill': ' **kiss**', 'murder': '**Michelle Yobama**', 'prison': '**your sweet home**', 'retarded': '**smart guy**',
                          'retard': '**wholesome guy**', 'dumb': '**super smart**', 'death': '**heaven**', 'threat': '**wholesome mommy :)**', 'fake': '**heartwarming**',
                          ' lies': ' **wholesome words**', 'damnit': '**awesome**', 'damn': '**awesome**', 'wrong': '**wholesome**', 'asshole': "**most wholesome person I've seen in my entire life**", ' ass ': ' **beautiful peach** ', 'racist': '**professional racer**',
                          'idiot': '**smol cat**', 'spam': '**wholesome message**', 'cock': '**majestic birdy**', 'scam': '**wholesome message**', 'stupid': '**mesmerizing**',
                          'hell': '**beautiful heaven (ohh praise the mighty God !!!!)**', 'worse': '**even more wholesome**'}
    if comment.id not in cache:
        comment_text = comment.body
        for word, conversed in wholesome_codomain.items():
            while word in comment_text.lower():
                change = True
                index = comment_text.find(word)
                comment_text = comment_text[0:index] + \
                    conversed + comment_text[index+len(word):]

        if change == True:
            wholesome_conversion_message = f"Your comment is a bit (just a bit, don't worry:))) unwholesome  \n\nbelow is the wholesomeness correction for you \n\n---############---  \n\n{comment_text}"
            comment.reply(wholesome_conversion_message+bot_message)
            cache.append(comment.id)
            print(wholesome_conversion_message)


def goodwords_reply(comment):
    global count, cache, bot_message
    goodwords = ['love', 'I like', 'happy', 'cry', 'sad', 'wholesome', 'glad', 'gorgeous', 'bless', 'autism',
                 'favorites', 'favorite', 'best', 'mom', 'incredible', 'respectful', 'remarkable', 'chungus', 'nice', 'cute', 'majestic',
                 'amazing', 'fantastic', 'wish', 'god']
    wholesome_rating = random.randint(90, 100)
    goodwords_message = ['No matter what happened, remember, I love you :))',
                         'You are a very nice person!',
                         'I love you :))',
                         'Everyone loves you!!',
                         'You are a very wholesome person!!',
                         f"I've analyzed your comment history, and your Wholesome Rating® is {wholesome_rating}!!!!",
                         'Your mom loves you, and so do I o((>ω< ))o',
                         'You have a beautiful mind!!!',
                         "I've been on reddit for 10 years, and you are the most wholesome person I've ever seen !!!!",
                         'your comment makes my day 😊😊',
                         'Your comment truly makes me wonder, in such a toxic society, how a person as wholesome as you still exist?',
                         "You're so wholesome that if you're a bot, I'll give you a 'good bot' vote!!!"]
    if comment.id not in cache:
        for word in goodwords:  # goes through our keywords
            if word in comment.body.lower():
                random.shuffle(goodwords_message)
                comment.reply(goodwords_message[0]+bot_message)
                cache.append(comment.id)
                print(goodwords_message[0])
                break


def negative_adjectives_reply(comment):
    global count, cache, bot_message
    negative_adjectives = ['tough', 'bad', 'tiring', 'hard', 'small', 'unstable', 'disrespectful', 'scam', 'ridiculous', 'stupid',
                           'dumb', 'retard', 'incompatible', 'inspiring', 'disrupted', 'loud', 'harsh', 'cruel', 'boring', 'tricky',
                           'permanent', 'abusive', 'common', 'shit', 'fucked', 'cringe', 'cringy', 'bullshit', 'impossible', 'false',
                           'smelly', 'dirty', 'disgusting', 'wrong', 'unhealthy']

    if comment.id not in cache:
        for word in negative_adjectives:  # goes through our keywords
            if word in comment.body.lower():
                # random.shuffle(goodwords_message)
                negative_adjectives_message = f"I know it might be {word}, but remember, you're the best!!!"
                comment.reply(negative_adjectives_message+bot_message)
                cache.append(comment.id)
                print(negative_adjectives_message)
                break


while True:
    for comment in subreddit.comments(limit=10):
        try:
            wholesome_spam(comment)
            # wholesome_conversion(comment)
            goodwords_reply(comment)
            negative_adjectives_reply(comment)
        except:
            print('blocked i guess')
            time.sleep(70)

            # pass

    if len(cache) > 30:
        del cache[0]

    time.sleep(10)
    # if count > 10:
    # sys.exit()
