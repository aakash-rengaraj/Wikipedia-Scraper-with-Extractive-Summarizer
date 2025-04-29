# Wikipedia-Scraper-with-Extractive-Summarizer
Vibe
# 📰 Wikipedia Article Extractive Summarizer

This is a Python-based extractive summarizer for **Wikipedia articles**. Given a valid Wikipedia article URL, it scrapes the text, processes it, and returns the most informative sentences based on word frequency. It's a great starter project for learning **web scraping**, **natural language processing**, and **basic text summarization techniques**.

---

## 📌 Features

- Scrapes text content from any Wikipedia article.
- Tokenizes text into sentences.
- Calculates word frequency, ignoring common stopwords.
- Scores sentences based on average word frequency.
- Outputs the top N key sentences as a summary.

---

## 📦 Requirements

Install these with pip:

pip install nltk numpy requests beautifulsoup4
You'll also need to download NLTK's stopwords corpus:

python
Copy
Edit
import nltk
nltk.download('stopwords')


🚀 Usage
Run the script with:

bash
Copy
Edit
python summarizer.py
Then follow the prompts:

Enter a valid Wikipedia URL (e.g., https://en.wikipedia.org/wiki/Portland_spy_ring)

Choose how many top-priority sentences you want in the summary.

🔍 Example Output
text
Copy
Edit
Enter Wiki Pedia URL: https://en.wikipedia.org/wiki/Portland_spy_ring
Enter your number of priorities: 3

Extractive Summarization:
1. The Portland Spy Ring was a Soviet espionage group...
2. It operated in Britain during the height of the Cold War...
3. The group was uncovered by MI5 in the early 1960s...
🛠️ How It Works
Uses BeautifulSoup to scrape <p> elements from the Wikipedia article.

Filters and tokenizes text using NLTK.

Calculates a frequency dictionary for all non-stopword words.

Scores each sentence based on the average frequency of its words.

Sorts and displays the top N scoring sentences.

🧠 What You’ll Learn
This project is great for learning about:

Web scraping and DOM parsing

Stopword filtering and tokenization

Text summarization basics

Using Python libraries like NLTK, NumPy, Requests, and BeautifulSoup
