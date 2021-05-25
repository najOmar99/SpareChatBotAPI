import json

from flask import Flask, render_template, request, redirect
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import date
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.debug = True
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
# training the bot
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("message.html", datetime=str(date.today()))


@app.route("/get_bot_response", methods=["GET", "POST"])
def get_bot_response():
    # userText = request.POST('msg')
    userText = request.form['msg']
    print(request.form['msg'])
    # userText = request.form['msg']
    data = english_bot.get_response(userText)
    print(data)
    data = str(english_bot.get_response(userText))
    # return str(english_bot.get_response(userText))
    json_data = jsonify(data)
    return json_data
    # return json.dumps([{'success':True, 'data': data}]), 200, {'ContentType':'application/json'}
    # return redirect ("message.html")


@app.route("/sendBot_answer")
def sendBot_answer(json_data):
    return redirect('http://localhost:8080', code=301)


if __name__ == '__main__':
    app.run()
