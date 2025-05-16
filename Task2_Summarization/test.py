import nltk

# Ensure 'punkt' is downloaded
nltk.download('punkt')

# Ensure 'stopwords' is downloaded
nltk.download('stopwords')

# Check if they exist in nltk_data
print(nltk.data.find('tokenizers/punkt'))
print(nltk.data.find('corpora/stopwords'))
