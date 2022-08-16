import tensorflow
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from tensorflow.keras.models import load_model
app = FastAPI()


with open('covid_token.pickle', 'rb') as handle:
  tokenizer = pickle.load(handle)

class Data(BaseModel):
    text : str

def loadModel():
    global predict_model

    predict_model = load_model('model.h5')

loadModel()

async def predict(data: Data):
    word_en=tokenizer.texts_to_sequences(data.text)
    X_new = pad_sequences(word_en, truncating='post',padding='post',maxlen =200)

    res = (predict_model.predict(X_new)>0.5).astype('int32')[:,0]
    function_to_np = lambda x : "Positive" if x == '0' else "Negative"
    output = function_to_np(res)
    return output

@app.post('/getclass/')
async def get_class(data: Data):
    category= await predict(data)
    res = {'sentiment': category}
    return {'results': res}

try:
    get_class()
except:
    print("can not post")
    