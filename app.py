from flask import Flask, render_template, request, jsonify
import random
import re
import pickle
import numpy as np
from chatbot import USER_INTENT, loaded_intent_CV, loadedIntentClassifier, getEntities, intent_label_map

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_text = request.json['user_text']
    query = re.sub('[^a-zA-Z]', ' ', user_text)
    query = query.split(' ')
    processed_text = [ps.stem(word.lower()) for word in query]  # Assuming ps is defined somewhere
    processed_text = loaded_intent_CV.transform([processed_text]).toarray()
    predicted_Intent = loadedIntentClassifier.predict(processed_text)
    result = np.argmax(predicted_Intent, axis=1)
    for key, value in intent_label_map.items():
        if value == result[0]:
            USER_INTENT = key
            break
    for i in intents['intents']:
        if i['tag'] == USER_INTENT:
            response = random.choice(i['responses'])
            entities = getEntities(query)  # Assuming getEntities is defined somewhere
            token_entity_map = dict(zip(entities, query))
            response = response.format(**token_entity_map)
            return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
