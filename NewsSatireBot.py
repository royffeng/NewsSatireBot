import praw
#reddit api login credentials
reddit = praw.Reddit(client_id = '<redacted>',
                     client_secret = '<redacted>',
                     username = 'AdvancedIQ',
                     password = '<redacted>',
                     user_agent = 'NewsSatireBot')
#import json
#import time
#import os

subreddit = reddit.subreddit('testingground4bots')

#summon phrase
phrase = '!enlightenme'

#original text list
originalList = ['witnesses', 'allegedly', 'new study', 'rebuild', 'space', 'google glass', 'smartphone', 'electric',
                'senator', 'car', 'election', 'congressional leaders', 'homeland security', 'could not be reached for comment',
                'debate', 'self driving', 'poll', 'candidate', 'drone', 'vows to', 'at large', 'successfully', 'expands',
                'first-degree', 'second-degree', 'third-degree', 'an unknown number', 'front runner', 'global', 'years',
                'minutes', 'no indication', 'urged restraint by', 'horsepower', 'gaffe', 'ancient', 'star-studded',
                'remains to be seen', 'silver bullet', 'subway system', 'surprising', 'war of words', 'tension', 'cautiously optimistic',
                'doctor who', 'win votes', 'behind the headlines', 'email', 'facebook post', 'tweet', 'facebook ceo', 'latest',
                'disrupt', 'meeting', 'scientists']

#substitutions list
subList = ['THESE DUDES I KNOW', 'KINDA PROBABLY', 'TUMBLR POST', 'AVENGE', 'SPAAAAAAAACE', 'VIRTUAL BOY', 'POKEDEX',
           'ATOMIC', 'ELF-LORD', 'CAT', 'EATING CONTEST', 'RIVER SPIRITS', 'HOMESTAR RUNNER', 'IS GUILTY AND EVERYONE KNOWS IT',
           'DANCE-OFF', 'UNCONTROLLABLE SWERVING', 'PSYCHIC READING', 'AIRBENDER', 'BIRD', 'PROBABLY WON\'T', 'VERY LARGE',
           'SUDDENLY', 'PHYSICALLY EXPANDS', 'FRIGGIN\' AWFUL', 'LIKE HUNDREDS', 'BLADE RUNNER', 'SPHERICAL', 'MINUTES',
           'YEARS', 'LOTS OF SIGNS', 'DRUNKENLY EGGED ON', 'TONS OF HORSEMEAT', 'MAGIC SPELL', 'HAUNTED', 'BLOOD-SOAKED',
           'WILL NEVER BE KNOWN', 'WAY TO KILL WEREWOLVES', 'TUNNELS I FOUND', 'SURPRISING (BUT NOT TO ME)', 'INTERPLANETARY WAR',
           'SEXUAL TENSION', 'DELUSIONAL', 'THE BIG BANG THEORY', 'FIND POKEMON', 'BEYOND THE GRAVE', 'POEM', 'POEM', 'POEM',
           'THIS GUY', 'FINAL', 'DESTROY', 'MENAGE A TROIS', 'CHANNING TATUM AND HIS FRIENDS']

def convert(lst):
    return (lst[0].split())

def checkList(sentence):
    listSentence = [sentence]
    word = convert(listSentence)
    newSentence = ""
    for i in range(len(word)):
        if word[i] in originalList:
            if word[i] == '.':
                i = i + 1
            else:
                indexPos = originalList.index(word[i])          
                newSentence += subList[indexPos] + " "
        else:
            newSentence += word[i] + " "
    return newSentence

for comment in subreddit.stream.comments():
    #checks the phrase to call bot
    parent = comment.parent()
    if phrase in comment.body:
        sentence = parent.body.replace(phrase, ' ')
        #attempts bots actions
        try:
            newWord = checkList(sentence)
            comment.reply(newWord)
            print("Posted")
        except:
            print("to frequent")
