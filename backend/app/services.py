from transformers import pipeline
from keybert import KeyBERT
import spacy

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Initialize KeyBERT model
kw_model = KeyBERT()

def generate_summary(text, summarizer=None):
    if not summarizer:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    try:
        # Summarizing the text with max and min length constraints
        summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        raise Exception(f"Error generating summary: {str(e)}")

def extract_keywords(text, use_keybert=True, num_keywords=5):
    if use_keybert:
        # Extracting keywords using KeyBERT
        keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=num_keywords)
        return [kw[0] for kw in keywords]
    else:
        # Using spaCy to extract noun chunks
        doc = nlp(text)
        keywords = [chunk.text for chunk in doc.noun_chunks]
        return list(set(keywords))[:num_keywords]

def generate_flashcards(text):
    # Extract keywords from the text
    keywords = extract_keywords(text)
    # Log the extracted keywords (for debugging purposes)
    print("Extracted Keywords:", keywords)
    # Create flashcards from keywords
    flashcards = [{"term": kw, "definition": f"Definition of {kw}"} for kw in keywords]
    return flashcards

def generate_quiz_questions(text, question_generator=None):
    if not question_generator:
        # Initializing a T5 model for question generation if not provided
        question_generator = pipeline('text2text-generation', model='t5-small')
    try:
        # Generating questions from the text with beam search to allow multiple outputs
        questions = question_generator(
            f"Generate questions based on the following text: {text}",
            max_length=100,
            num_return_sequences=3,
            num_beams=3  # Enables beam search
        )
        
        # Creating a list of questions with placeholder answers
        return [{"question": q['generated_text'], "answer": "Answer to the question"} for q in questions]
    except Exception as e:
        raise Exception(f"Error generating quiz questions: {str(e)}")

