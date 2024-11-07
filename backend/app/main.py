from fastapi import FastAPI, HTTPException
from app.schemas import NoteRequest, SummaryResponse, FlashcardsResponse, QuizResponse
from app.models import load_models
from app.services import generate_summary, generate_flashcards, generate_quiz_questions
from fastapi.middleware.cors import CORSMiddleware
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Allow requests from frontend's origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this if frontend runs on a different port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models when the app starts
summarizer, question_generator = load_models()

@app.post("/summarize", response_model=SummaryResponse)
async def summarize(note: NoteRequest):
    try:
        logger.info(f"Summarizing note with {len(note.text)} characters.")
        summary = generate_summary(note.text, summarizer)
        return {"summary": summary}
    except Exception as e:
        logger.error(f"Error in summarizing note: {str(e)}")
        raise HTTPException(status_code=500, detail="Error in summarizing note")

@app.post("/flashcards", response_model=FlashcardsResponse)
async def flashcards(note: NoteRequest):
    try:
        logger.info(f"Generating flashcards for note with {len(note.text)} characters.")
        flashcards = generate_flashcards(note.text)
        return {"flashcards": flashcards}
    except Exception as e:
        logger.error(f"Error in generating flashcards: {str(e)}")
        raise HTTPException(status_code=500, detail="Error in generating flashcards")

@app.post("/quiz", response_model=QuizResponse)
async def quiz(note: NoteRequest):
    try:
        logger.info(f"Generating quiz questions for note with {len(note.text)} characters.")
        questions = generate_quiz_questions(note.text, question_generator)
        return {"questions": questions}
    except Exception as e:
        logger.error(f"Error in generating quiz questions: {str(e)}")
        raise HTTPException(status_code=500, detail="Error in generating quiz questions")
