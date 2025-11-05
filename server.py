"""
Flask server for Emotion Detection application
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main application page"""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Endpoint for emotion detection
    Receives text to analyze via query parameter and returns formatted response
    """
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion_detector function from the package
    response = emotion_detector(text_to_analyze)
    
    # Extract the emotion scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Format the response as requested
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

