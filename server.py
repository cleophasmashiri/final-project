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
        
