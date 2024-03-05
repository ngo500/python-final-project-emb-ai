from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

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