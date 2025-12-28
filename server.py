from flask import Flask, render_template, request
from EmotionDetection.emotion_detection inport emotion_detector

app = Flask(__name__)

@app.route('/')
def show_index():
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector():
    text = request.args.get('text')
    res = emotion_detector(test)
    return f"For the given statement, the system response is 'anger': {res['anger']}, 'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}. The dominant emotion is {res['dominant_emotion']}."