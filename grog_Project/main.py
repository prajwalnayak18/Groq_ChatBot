from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(f"GROQ_API_KEY: {GROQ_API_KEY}")  # Check API key

client = Groq(api_key=GROQ_API_KEY)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Groq API"}

@app.post("/ask")
async def ask_question(question: Question):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question.question,
                }
            ],
            model="llama3-8b-8192",
        )
        answer = chat_completion.choices[0].message.content
    except Exception as e:
        answer = f"Failed to get answer from Groq API: {e}"
    return {"answer": answer}
