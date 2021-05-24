from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from datetime import date

app = Flask(__name__)
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
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))
    # return redirect ("message.html")



if __name__ == '__main__':
    app.run()
