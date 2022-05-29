import numpy as np
import pickle
import random
import json
from keras.models import load_model
import nltk

from nltk.stem import WordNetLemmatizer

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(
        word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return(np.array(bag))


def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result



def chatbot_response(msg):
    ints = predict_class(msg, model)
    print(msg, ints)
    try:
        if(float(ints[0]['probability']) > 0.79):  # 79
            print("in accept by probability ")
            res = getResponse(ints, intents)
        elif(len(ints) == 1):
            print("in accept by scarcity ")
            res = getResponse(ints, intents)
        else:
            print("in reject ")
            res = "Umm, sorry I coundn't process it. Would you mind changing the words a bit so that I can interpret it correctly. I am not that smart you see."
    except:
        print("Exception")
        res = "Umm, sorry I coundn't process it. Would you mind changing the words a bit so that I can interpret it correctly. I am not that smart you see."
    return res
