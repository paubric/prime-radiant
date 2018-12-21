from textblob import TextBlob

def scan(text):
    blob = TextBlob(text)
    results = {
        "pol": blob.sentiment.polarity,
        "sub": blob.sentiment.subjectivity
    }
    return results
