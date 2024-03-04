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
    
    #send info over POST request and return response text
    response = requests.post(url, json = myobj, headers = header, timeout = 10)
    return response.text
    