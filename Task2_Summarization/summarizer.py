import nltk
import re
import heapq
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

try:
    nltk.data.find('tokenizers/punkt/english.pickle')
except LookupError:
    print("Downloading punkt tokenizer...")
    nltk.download('punkt')
    print("punkt tokenizer downloaded.")

try:
    nltk.data.find('corpora/stopwords/english')
except LookupError:
    print("Downloading stopwords...")
    nltk.download('stopwords')
    print("stopwords downloaded.")


def extractive_summary(text, num_sentences=3):
    # Tokenize sentences
    sentences = sent_tokenize(text)
    
    if len(sentences) <= num_sentences:
        return " ".join(sentences)  # If text is too short, return as is

    # Remove special characters and tokenize words
    word_frequencies = {}
    stop_words = set(stopwords.words("english"))

    for sentence in sentences:
        cleaned_sentence = re.sub(r'\W', ' ', sentence.lower())  # Clean sentence
        words = word_tokenize(cleaned_sentence)  # Tokenize words
        for word in words:
            if word not in stop_words:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Normalize word frequencies
    max_freq = max(word_frequencies.values(), default=1)  # Handle empty dict case
    word_frequencies = {word: freq / max_freq for word, freq in word_frequencies.items()}

    # Rank sentences based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        sentence_word_count = word_tokenize(sentence.lower())
        sentence_scores[sentence] = sum(word_frequencies.get(word, 0) for word in sentence_word_count)

    # Get the top N sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    return " ".join(summary_sentences)

# Example Usage
if __name__ == "__main__":
    text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural intelligence 
    displayed by animals and humans. Leading AI textbooks define the field as the study of "intelligent agents":
    any system that perceives its environment and takes actions that maximize its chance of achieving its goals.
    Some popular applications of AI include language translation, image recognition, and autonomous vehicles.
    AI research has led to significant improvements in healthcare, finance, and many other industries.
    """
    
    summary = extractive_summary(text, num_sentences=2)
    print("Summary:\n", summary)
