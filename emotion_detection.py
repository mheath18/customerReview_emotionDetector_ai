import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP Library URL for Emotion Predict
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input JSON for the request
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make POST request to Watson NLP API
    response = requests.post(url, json=input_json, headers=headers)

    # Convert the response text into a dictionary using json library
    response_dict = json.loads(response.text)

    # Extract the required set of emotions from the response
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Extract individual emotion scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Create a dictionary with emotion scores
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Find the dominant emotion (emotion with the highest score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Add the dominant emotion to the result
    emotion_scores['dominant_emotion'] = dominant_emotion

    # Return the formatted output
    return emotion_scores
