from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

def scan(text):
    blob = TextBlob(text)
    results = {
        "pol": round(blob.sentiment.polarity, 3),
        "sub": round(blob.sentiment.subjectivity, 3)
    }

    return results

def url_to_text(url):
    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html, 'lxml')

    text = []
    for tag in soup.find_all('p'):
        text.append(tag.text)
        tag.next_sibling

    text = ''.join(text)
    return text
