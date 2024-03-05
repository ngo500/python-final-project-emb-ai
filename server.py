from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detect():
    """
    function that receives text from the HTML interface and 
    uses emotion_detector() to analyze what emotions are 
    present, and what the dominant emotion of the text is
    returns:
    string that gives the calculated percentage of each emotion,
    and the calculated dominant emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return f"""For the given statement, the system response is: 'anger':{anger}, 
    'disgust':{disgust}, 'fear':{fear}, 'joy':{joy}, and 'sadness':{sadness}. 
    The dominant emotion is <b>{dominant_emotion}</b>."""

@app.route("/")
def render_index_page():
    """
    function that renders the index.page
    returns:
    always renders the index.html page
    """
    return render_template('index.html')

if __name__ == "__main__":
    #executes the flask app and deploys it on localhost:5000
    app.run(host = "0.0.0.0", port = 5000)