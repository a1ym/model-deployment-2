
from flask import Flask, request, jsonify
from textblob import TextBlob

import csv
import tensorflow as tf
import tensorflow_text as text
import numpy as np


app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    text = str(text)

    
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        sentiment_label = 'Positive'
    elif sentiment < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    response = {
        'sentiment': sentiment,
        'sentiment_label': sentiment_label
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()



