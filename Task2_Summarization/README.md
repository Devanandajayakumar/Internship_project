# Task 2: Extractive Text Summarization

## Overview
This project performs extractive text summarization using basic NLP techniques. It allows users to input any text and receive a condensed version by selecting key sentences based on word frequency.

## Tech Stack
- Python
- NLTK (Natural Language Toolkit)
- Streamlit

## Features
- Streamlit UI for summarization
- Customizable summary length
- Uses sentence and word tokenization
- Removes stopwords and scores sentences

## Folder Structure
```
task2_summarizer/
│
├── app.py                 # Streamlit app
├── summarizer.py          # Contains extractive summarization logic
├── test.py                # Validates NLTK data setup
├── task2_summarizer.ipynb # Model training/demo notebook
├── requirements.txt       # Required libraries
└── __pycache__/           # Auto-generated Python bytecode
```

## How to Run
### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Ensure NLTK data is downloaded
```bash
python test.py
```

### 3. Run Streamlit app
```bash
streamlit run app.py
```

## Model Details
This is a rule-based model (not ML-trained), so **no .pkl or h5 saved model** is needed. It uses:
- Word frequency scores
- NLTK’s `sent_tokenize` and `stopwords`

## Evaluation
- This is a basic extractive summarization model.
- No accuracy or confusion matrix metrics as it is unsupervised and not trained on labels.

