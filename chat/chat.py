import random
import json
import pickle
import numpy as np
import nltk

#Load the trained model and make predictions for new sentences:

""" Random: donne accès à des fonctions prenant en charge de nombreuses opérations. La chose la plus importante 
est peut-être qu'elle vous permet de générer des nombres aléatoires.
"""

# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('punkt')
from nltk.stem import  WordNetLemmatizer
from tensorflow.python.keras.models import load_model

lemmatizer=WordNetLemmatizer()
with open('chat', 'r', encoding='utf-8') as file:
    intents = json.load(file)

words=pickle.load(open('chat','rb'))
classes=pickle.load(open('chat','rb'))
model=load_model('chat')

def clean_up_sentence(sentence):
    sentence_words=nltk.word_tokenize(sentence)
    return sentence_words
def bag_of_words(sentence):
    bag=[0]*len(words)
    for w in sentence_words:
        for i ,word in enumerate(words):
            if word == w :
                bag[i] = 1
    return np.array(bag)
def predict_class(sentence):
    results=[[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    return_list=[]
    for r in results:
        return_list.append({'intent':classes[r[0]],'probability':str(r[1])})
    return return_list
def get_response(intents_list,intents_json):
    try:
        if float(intents_list[0]['probability'])>0.4 :
            list_of_intents=intents_json['intents']
            for i in list_of_intents:
                if i['tag']==tag:
                    return random.choice(i['responses'])
    except:
        pass
                # break
    if ('english' in intents_list[0]['intent'])==True:
        return " I do not understand..."
    if ('french' in intents_list[0]['intent'])==True:
        return " Je ne comprends pas..."
    if ('tounsi' in intents_list[0]['intent'])==True:
        return " Manich nefhem fik 3awed ektebli..."



