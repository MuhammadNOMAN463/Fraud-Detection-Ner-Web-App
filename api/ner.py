from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp = spacy.load("en_core_web_sm")

class TextRequest(BaseModel):
    text: str

@app.post("/ner")
async def ner_analysis(request: TextRequest):
    doc = nlp(request.text)
    entities = [
        {"text": ent.text, "label": ent.label_}
        for ent in doc.ents
        if ent.label_ in ["PERSON", "ORG", "GPE", "DATE", "MONEY"]
    ]
    return {"entities": entities}