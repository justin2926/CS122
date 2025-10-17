import re
import pandas as pd
from textblob import TextBlob

def extract_hashtags(text):
    pattern = re.compile(r'#[A-Za-z0-9]+')
    match = pattern.search(text)
    return pattern.findall(text)

def extract_mentions(text):
    pattern = re.compile(r'@[A-Za-z0-9]+')
    match = pattern.search(text)
    return pattern.findall(text)

def clean_post_content(text):
    pattern = re.compile('htt[p|ps]+://[A-Za-z0-9]+.[a-z]+|^@[A-Za-z0-9]+|@[A-Za-z0-9]+|#[A-Za-z0-9]+|[!?,._-]|[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF]|[\U00002700-\U000027BF]|[\U0001F900-\U0001F9FF]|[\U00002600-\U000026FF]|[\U00002B00-\U00002BFF]', re.UNICODE)
    match = pattern.search(text)

    if match:
        return pattern.sub("", text)

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = float(blob.sentiment.polarity)

    return polarity

def get_avg_engagement(df):
    newDF = df.groupby('user_id').agg(
        likes = ('likes', 'mean'),
        shares = ('shares', 'mean')
    )

    return newDF



