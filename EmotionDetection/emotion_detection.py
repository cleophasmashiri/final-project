import requests
import json

def getResultValue(res, key):
    return res['emotionPredictions'][0]['emotion'][key]

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_text = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json = json_text)
    response_json = json.loads(response.text)
    keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    formattedRes = {'dominant_emotion': None}
    for k in keys:
        formattedRes[k] = getResultValue(response_json, k)
        dominant_emotion = formattedRes['dominant_emotion']
        if dominant_emotion == None or formattedRes[dominant_emotion] < formattedRes[k]:
            dominant_emotion = k
            formattedRes['dominant_emotion'] = k
