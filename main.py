from bs4 import BeautifulSoup
import requests
import nltk
import numpy
nltk.download('stopwords')

def get_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    content = soup.find(id="mw-content-text")
    paragraph = content.find_all('p')
    final_content = ""
    for i in paragraph:
        final_content += i.text.strip()
    return nltk.tokenize.sent_tokenize(final_content, language='english')

def get_link():
    url = input("Enter Wiki Pedia URL: ")
    if url.startswith("https://en.wikipedia.org/wiki")==True:
        return url
    else:
        print("Please enter a valid \"https://en.wikipedia.org/wiki\" URL!!!")

# sort_dictbyvalue() sorts dictionary on descending order based on values.
def sort_dictbyvalue(dictionary):
    key = list(dictionary.keys())
    value = list(dictionary.values())
    sorted_index = numpy.argsort(list(value))[::-1]
    sd = {}
    for i in sorted_index:
        sd[key[i]] = value[i]
    return sd

# frequency() returns the word frequency without counting stopwords
def frequency(data):
    frequency = {}
    stop_words = set(nltk.corpus.stopwords.words('english'))
    for sentence in data:
        for word in nltk.tokenize.word_tokenize(sentence):
            if word.lower() not in stop_words and word.isalnum():
                if word.lower() in frequency:
                    frequency[word.lower()] += 1
                else:
                    frequency[word.lower()] = 1
    return frequency


'''
score(frequency, data) returns a score based on the below formula.
final_score = sentence_score/length
   | |-> sentence_score is the summation of word*word_frequency given that the word is not a stopword
   |_|-> length is the number of non-stopwords in the sentence
'''
def score(f, data):
    out = {}
    for sentence in data:
        sentence_score = 0
        length = 0
        words = nltk.tokenize.word_tokenize(sentence)
        for word in words:
            if word.lower() in f:
                sentence_score += f[word.lower()]
                length += 1
        if length == 0:
            final_score = 0
        else: 
            final_score = sentence_score/length
        out[sentence] = final_score
    return sort_dictbyvalue(out)

#Main Block
def main():
    data = get_content(get_link())
    f = frequency(data)
    scored_content = list(score(f, data).keys())
    print("Extractive Summarization: ")
    for i in range(0,int(input("Enter your number of priorities: "))):
        if i<len(scored_content):
            print(scored_content[i])

#############
main()
#############