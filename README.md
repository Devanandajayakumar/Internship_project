**Intern Name:** Devananda K J  
**Internship Duration:** 16-Jan-2025 to 16-May-2025  
**Email:** devanandakjayakumar@gmail.com

---

## Project Overview

This repository contains three separate machine learning tasks developed during my internship at NullClass. Each task focuses on different ML concepts and implementations, showcasing skills in data analytics, natural language processing, and chatbot development.

---

## Repository Structure

/Internship
│
├── task1_analytics/
│ ├── task1_analytics.ipynb
│ ├── dashboard.py
│ ├── config.py
│ ├── db_logger.py
│ ├── requirements.txt
│
├── task2_summarizer/
│ ├── app.py
│ ├── summarizer.py
│ ├── test.py
│ ├── requirements.txt
│
├── task3_chatbot/
│ ├── chatbot.py
│ ├── database.py
│ ├── retriever.py
│ ├── ui.py
│ ├── requirements.txt
│ ├── /data
│ ├── chromadb
│ └── sqlite3 (database files)
│
├── .env (common environment variables for all tasks)
├── .gitignore
└── README.md



---

## Setup Instructions

### Prerequisites

- Python 3.8 or above
- Git
- Virtual environment tool (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/internship-project.git
   cd internship-project
2.Create and activate a virtual environment (optional but recommended):
 
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows  
3.Install dependencies for each task by navigating into the task folder and running:
  
       pip install -r requirements.txt


How to Run Each Task
Task 1 - Data Analytics Dashboard
Open and run task1_analytics/task1_analytics.ipynb in Jupyter Notebook for the training and analysis.

Run dashboard.py to launch the analytics dashboard.

Task 2 - Extractive Text Summarizer
Run app.py using Streamlit:
   
   streamlit run task2_summarizer/app.py

      
The chatbot uses a custom vector database (ChromaDB) and semantic search to answer queries dynamically.

Add knowledge through the sidebar to expand the chatbot’s responses.
