import requests
import json
import urllib.parse
import os
import sys

# Zidan ganteng B)
# Tested on windows & kali linux

url = "https://chat.ai.cneko.org/"

def cihuy():
    if (sys.platform == "linux"):
        os.system('clear')
    else:
        os.system('cls')
    print("Api: "+url)
    print('')

def getResponse(res):
    print(res['response']+"\n")

def sendMessage(msg):
    req = requests.get(url+"?t="+urllib.parse.quote_plus(msg))
    getResponse(req.json())

def main():
    userInput = input(">> ")
    sendMessage(userInput)
    main()

cihuy()
main()