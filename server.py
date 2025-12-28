"""
Emotion Detection Server

This module defines a Flask-based web server that provides an API 
for detecting emotions in text using the EmotionDetection library.
It handles requests for single-statement analysis and returns 
formatted scores for joy, anger, fear, sadness, and disgust.

Usage:
    python3 server.py

Routes:
    - /emotionDetector: GET request containing text to analyze.
    - /: Renders the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def show_index():
    """
    Renders the main application page.

    This function handles the root route ('/') and serves the 
    index.html template, which contains the user interface 
    for the emotion detection tool.

    Returns:
        Response: The rendered HTML content for the home page.
    """
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_():
    """
    Analyzes the text input provided by the user and returns emotion scores.

    This function retrieves the text to be analyzed from the request arguments,
    calls the emotion detection service, and formats the output. If the input 
    is invalid or the service fails, it returns a 400 error message.

    Returns:
        str: A formatted string containing the breakdown of all emotions 
             and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if res.get('anger') is None:
        return 'Invalid text! Please try again!.'
    return f"""For the given statement, the system response is 'anger': {res['anger']},
     'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy'
     : {res['joy']} and 'sadness': {res['sadness']}. The dominant 
     emotion is {res['dominant_emotion']}."""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
