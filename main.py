from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from pytz import timezone
import pytz
import datetime
import wikipedia
import pyjokes
import emoji
import os
import random
import requests
import json
import string

#  pip install chatterbot==1.0.2
app = Flask(__name__)  # Create an Instance
english_bot = ChatBot("ChatterBot",
                      storage_adapter="chatterbot.storage.SQLStorageAdapter")

#trainig the data
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")


@app.route('/')  # Route the Function
def main():  # Run the function
    return render_template('index.html')  #to send conxete to html


@app.route('/get')
def get_bot_response():
    userText = request.args.get("msg")
    print(str(userText))
    small = userText.lower()
    if "time" in small:
        yet = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata'))) #time for asia/india check py time zones for the time zones
        return "Time is " + yet
    elif "joke" in small:
        return str(pyjokes.get_joke())
    elif "help" in small:
      naman=str(random.choice(["hello","nice to meet you","HI","oh!! help is right here","Let's see","hey"]))
      new=str(" User\n\n you can use chat bot to have normal conversations like, aking time, jokes,quotes and much more\n to know more about the chatbot check for code by asking for he bot\n\n.  To generate random password just type PASSWORD length NOTE: WE ARE WOKING ON THE DOCUMENTATION PAGE")
      hi=naman+new
      return hi
    elif "password" in small:
      try:
        num = [int(word) for word in small.split() if word.isdigit()]
        lon = num[0]
        password = ''.join(random.choice(string.printable) for i in range(lon))
        return password
      except:
        password = ''.join(random.choice(string.printable) for i in range(8))
        return password
    elif small in ["hi","hello"]:
      aman=str(random.choice(["!!!","nice to meet you","how may I help you","User"]))
      yet = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
      seo=int(yet[11:13])
      print(seo)
      if seo>=0 and seo<12:
        new=str("Good morning ")
        nama=str(aman)
        kai=new+nama
        return kai
      elif seo>=12 and seo<16:
        new=str("Good afternoon ")
        nama=str(aman)
        kai=new+nama
        return kai
      elif seo>=16 and seo<19:
        new=str("Good evening ")
        nama=str(aman)
        kai=new+nama
        return kai 
      elif seo>=19 and seo<22:
        new=str("Good night ")
        nama=str(aman)
        kai=new+nama
        return kai
      else: 
        return "Good night have a nice sleep"
    elif "random" in small:
        try:
            num = [int(word) for word in small.split() if word.isdigit()]
            fi = num[0]
            se = num[1]
            return str(random.randrange(fi, se))
        except:
            return str("random number>", random.randrange(0, 1000),
                       "<(Predefined range/Default Range)")
    elif "who is" in small:
        person = small.replace('who is', '')
        return str(wikipedia.summary(person, 1))
    elif "created you" in small:
        return emoji.emojize("Naman :red_heart:")
    elif "wikki" in small:
        word = small.replace("wikki", "")
        if "search" in word:
            sear = word.replace('search', '')
            return str(wikipedia.search(sear))
        elif "page" in word:
            try:
                seaar = word.replace('page', '')
                ny = wikipedia.summary(seaar)
                return str(ny)
            except:
                return "Result not found!!(try typing wikki search ____)"
        else:
            return emoji.emojize(
                "sorry :face_with_monocle: use page or search with this")
    elif "quote" in small:
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return str(quote)
    else:
        return str(english_bot.get_response(userText))


#hosts at the ip
app.run(host='0.0.0.0', port=5000, debug=True)
