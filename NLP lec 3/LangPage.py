from fastapi import FastAPI
from pydantic import BaseModel
import re
from pickle import load

# Load your models
with open("Countvector.pkl", "rb") as f:
    cv = load(f)

with open("LangModel.pkl", "rb") as f:
    model = load(f)

app = FastAPI(title="Language Detector")

# Pydantic model
class TextInput(BaseModel):
    text: str

def clean_function(text):
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'http\S+|www\S+|@\S+', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@app.post("/detect")
def detect_language(input_data: TextInput):
    clean_text = clean_function(input_data.text)
    vector_text = cv.transform([clean_text])
    result = model.predict(vector_text)
    return {"output": result[0]}
