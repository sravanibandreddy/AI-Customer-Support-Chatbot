import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ CSV
faq_df = pd.read_csv("faq.csv")

# Vectorize questions
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(faq_df['Question'])

def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vector, question_vectors)
    best_match_idx = similarity.argmax()
    best_score = similarity[0][best_match_idx]

    if best_score < 0.3:  # threshold for “too different”
        return "Sorry, I don't know the answer to that question."
    else:
        return faq_df['Answer'][best_match_idx]