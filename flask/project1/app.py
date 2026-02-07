from flask import *
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
app=Flask(__name__)
nlp=spacy.load("en_core_web_lg")

def extract_pdf_text(pdf):
    reader=PdfReader(pdf)
    text=""
    for page in reader.pages:
        text=text+page.extract_text()

    return text

def clean_text(text):
    text=text.lower()
    text=nlp(text)
    text=[t for t in text]
    text=[t for t in text if not t.is_punct]
    text=[t for t in text if not t.is_stop]
    text=[t.lemma_ for  t in text]
    text=[str(t) for t in text]
    text=" ".join(text)
    return text



@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        resume_pdf=request.files.get("resume_pdf")
        jd_pdf=request.files.get("jd_pdf")

        resume_text=extract_pdf_text(resume_pdf)
        jd_text=extract_pdf_text(jd_pdf)

        clean_resume=clean_text(resume_text)
        clean_pdf=clean_text(jd_text)

        tv=TfidfVectorizer()
        vectors=tv.fit_transform([clean_resume,clean_pdf])
        score=cosine_similarity(vectors[0],vectors[1])
        score=score[0][0]
        score=round(score,2)*100
        msg="Your score is "+str(score)
        return render_template("home.html",msg=msg)

    else:
        return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)
