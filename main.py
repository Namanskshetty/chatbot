from flask import Flask, render_template, request  # Import Flask Class, and render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from pytz import timezone
import pytz
import datetime
import wikipedia
import pyjokes
import emoji
import random
import os

app = Flask(__name__)  # Create an Instance
english_bot = ChatBot("ChatterBot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
                      

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
        yet = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata'))) #for timezone refer(https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
        return "Time is " + yet
    elif "joke" in small:
      return str(pyjokes.get_joke())
    elif "random" in small:
      try:
          num=[int(word) for word in small.split() if word.isdigit()]
          fi=num[0]
          se=num[1]
          return str(random.randrange(fi,se))
      except:
          return str("random number>",random.randrange(0,1000),"<(Predefined range/Default Range)")

    elif "who is" in small:
      person = small.replace('who is', '')
      return str(wikipedia.summary(person, 1))
    elif "created you" in small:
      return emoji.emojize("Naman :red_heart:")
    elif "wikki" in small:
      word= small.replace("wikki","")
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
        return emoji.emojize("sorry :face_with_monocle: use page or search with this")
    else:
      return str(english_bot.get_response(userText))


app.run(host='0.0.0.0', port=5000, debug=True)
