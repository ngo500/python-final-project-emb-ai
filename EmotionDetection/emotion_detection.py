""" function that sends data to Watson NLP BERT for emotion analysis """
import json
import requests

def emotion_detector(text_to_analyze):
    """
    function that takes given text, sends to Watson NLP, and receives 
    response, containing what emotions are being expressed in the text
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document" : { "text" : text_to_analyze } }
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    
    #send info over POST request and store response
    response = requests.post(url, json = myobj, headers = header, timeout = 10)
    #formated response as json, dictionary of dictionaries
    formatted_response = json.loads(response.text)
    #return formatted_response['emotionPredictions'][0]['emotion']['anger']

    #retrieve required set of emotions
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    #find the dominant emotion and store name
    emotions = {'anger' : anger, 'disgust' : disgust, 'fear' : fear,
    'joy' : joy, 'sadness' : sadness}
    dominant_emotion = max(emotions, key = emotions.get)

    #return the emotions, and the dominant emotion, from the response
    return { 'anger' : anger, 'disgust' : disgust, 'fear' : fear,'joy' : joy, 
    'sadness' : sadness, 'dominant_emotion' : dominant_emotion}
