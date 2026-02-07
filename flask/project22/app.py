from flask import * 
import spacy
from pickle import load
nlp = spacy.load("en_core_web_lg")
from reader import read_latest

f = open("model.pkl" , "rb")
model = load(f)
f.close()

f = open("vector.pkl" , "rb")
tv = load(f)
f.close()

import time
latest_body=None
def check_live():
    global latest_body
    while True:
        subject,body=read_latest()
        if body!=latest_body:
            latest__body=body
            clean_body=clean_function(body)
            vector_body=tv.transform([clean_body])
            result=model.predict(vector_body)[0]
            if result.lower() =="ham":
                result="Not Spam"
            print("New Mail found",body)
            print("Result is ",result)
        time.sleep(10)



def clean_function(text):
    text = text.lower()
    text = nlp(text)
    text = [t for t in text]
    text = [t for t in text if not t.is_punct]
    text = [t for t in text if not t.is_stop]
    text = [t.lemma_ for t in text]
    text = [str(t) for t in text]
    text = " ".join(text)
    return text

app = Flask(__name__)

import threading
started=None
@app.route("/live")
def live():
    global started
    if not started:
        started=True
        threading.Thread(target=check_live,daemon=True).start()
    return render_template("home.html",result="Live Analysis started")



@app.route("/check-recent")
def check():
    subject , body = read_latest()
    clean_text = clean_function(body)
    vector_body = tv.transform([clean_text])

    result = model.predict(vector_body)
    result = result[0]
    if result.lower() =="ham":
        result = "Not Spam"
    return render_template("home.html" , result = result , body=body)


@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text")
        clean_text = clean_function(text)
        vector_text = tv.transform([clean_text])
        result = model.predict(vector_text)
        result = result[0]
        if result.lower() =="ham":
            result = "Not Spam"
        return render_template ("home.html",result=result)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)