import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    response = requests.post(url, json={'raw_document': {'text': text_to_analyze}}, headers={'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}, timeout=30)
    if response.status_code == 400:
        return dict.fromkeys(('anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'))
    response.raise_for_status()
    emotions = response.json()['emotionPredictions'][0]['emotion']
    result = {name: emotions[name] for name in ('anger', 'disgust', 'fear', 'joy', 'sadness')}
    result['dominant_emotion'] = max(result, key=result.get)
    return result
