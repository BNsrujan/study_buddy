from transformers import pipeline

def load_models():
    # Load BART model for summarization and T5 model for question generation
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    question_generator = pipeline("text2text-generation", model="t5-small")
    return summarizer, question_generator
