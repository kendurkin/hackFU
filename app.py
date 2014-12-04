from flask import Flask, render_template,request,jsonify
import requests,json,twitter
from OAuthSettings import settings

consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']

api = twitter.Api(
    consumer_key = consumer_key,
    consumer_secret = consumer_secret, 
    access_token_key = access_token_key, 
    access_token_secret = access_token_secret)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry bruh, this page ain't here", 404

@app.route("/")
def hello():
    tweets = api.GetSearch('#LocalHackDay')
    return render_template("results.html",api_data=tweets)

@app.route("/_refresh")
def refresh_tweets():
    tweets = api.GetSearch('#LocalHackDay')
    return tweets

if __name__ == "__main__":
    app.run(host="0.0.0.0")
