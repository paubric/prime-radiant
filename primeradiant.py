from textblob import TextBlob

def metrics(text):
    blob = TextBlob(text)
    results = {
        "pol": blob.sentiment.polarity,
        "sub": blob.sentiment.subjectivity
    }
    return results
