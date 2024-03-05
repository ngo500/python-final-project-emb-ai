""" function that sends data to Watson NLP BERT for emotion analysis """
import json
import requests

def emotion_detector(text_to_analyze):
    """
    function that takes given text, sends to Watson NLP, and receives 
    response, containing what emotions are being expressed in the text
    """
    if not text_to_analyze:
        return { 'anger' : 'empty', 'disgust' : 'empty', 'fear' : 'empty',
        'joy' : 'empty', 'sadness' : 'empty', 'dominant_emotion' : 'empty' }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document" : { "text" : text_to_analyze } }
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    
    #send info over POST request and store response
    response = requests.post(url, json = myobj, headers = header, timeout = 10)
    #formated response as json, dictionary of dictionaries
    formatted_response = json.loads(response.text)
    #return formatted_response['emotionPredictions'][0]['emotion']['anger']

    if response.status_code == 200:
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
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    #return the emotions, and the dominant emotion, from the response
    return { 'anger' : anger, 'disgust' : disgust, 'fear' : fear,'joy' : joy, 
    'sadness' : sadness, 'dominant_emotion' : dominant_emotion}
