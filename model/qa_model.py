from transformers import pipeline

qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", clean_up_tokenization_spaces=True, device = -1)
