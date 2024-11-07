from pydantic import BaseModel
from typing import List, Optional

# Request Model for User Notes
class NoteRequest(BaseModel):
    text: str

# Response Model for Summarization
class SummaryResponse(BaseModel):
    summary: str

# Response Model for Flashcards
class FlashcardItem(BaseModel):  # Changed for clarity
    term: str
    definition: str

class FlashcardsResponse(BaseModel):
    flashcards: List[FlashcardItem]

# Response Model for Quiz Questions
class QuizQuestion(BaseModel):
    question: str
    answer: str

class QuizResponse(BaseModel):
    questions: List[QuizQuestion]
