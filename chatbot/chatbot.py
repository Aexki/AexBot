import random
import json
import pickle
import numpy as np
import os
import datetime
dt = datetime.datetime.now()

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model


lemmatizer = WordNetLemmatizer() 

path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chatbot')
intents = json.loads(open(path+'\intents.json').read())
words = pickle.load(open(path+'\words.pkl', 'rb'))
classes = pickle.load(open(path+'\classes.pkl', 'rb'))
model = load_model(path+'\chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word==w:
                bag[i]=1
    
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i , r in enumerate(res) if r> ERROR_THRESHOLD]
    
    results.sort(key=lambda x: x[1], reverse= True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            if(i['tag']=="age"):
                result = "He is "+ str(int(dt.year)-2000)+" years old!"
                break
            result = random.choice(i['responses'])
            break 
    return result

print("Go! The Bot is running!")

# while True:
#     message = input("Enter message for bot: ")
#     ints = predict_class(message)
#     res = get_response(ints, intents)
#     print(res)
        
        