from flask import Flask, render_template, request
import random
from main import SentimentAnalysis

app = Flask(__name__)

def analyze_sentiment(topic, num_tweets):
    obj = SentimentAnalysis()
    obj.DownloadData(topic, num_tweets)
    res = obj.polarity
    if (res >= 0 and res <= 0.3):
        return  "Neutral"
    elif (res > 0.3 and res <= 1):
        return  "Positive"
    return "negative"

def display_sentiment_emoji(sentiment):
    if sentiment == "positive":
        return "😊 Positive"
    elif sentiment == "negative":
        return "😔 Negative"
    else:
        return "😐 Neutral"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        num_tweets = int(request.form['num_tweets'])
        sentiment = analyze_sentiment(topic, num_tweets)  
        sentiment_emoji = display_sentiment_emoji(sentiment)
        return render_template("result.html", topic=topic, num_tweets=num_tweets, sentiment=sentiment_emoji)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
