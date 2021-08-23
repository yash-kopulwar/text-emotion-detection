import re
import string
from nltk.corpus import stopwords

# Text cleaning functions

# removing URLs

def remove_URL(text):
    text=str(text)
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub('', text)


# removing emojis

def remove_emojis(text):
    emojis = re.compile(
        '['
        u'\U0001F600-\U0001F64F'  # emoticons
        u'\U0001F300-\U0001F5FF'  # symbols & pictographs
        u'\U0001F680-\U0001F6FF'  # transport & map symbols
        u'\U0001F1E0-\U0001F1FF'  # flags
        u'\U00002702-\U000027B0'
        u'\U000024C2-\U0001F251'
        ']+',
        flags=re.UNICODE)
    return emojis.sub('', text)


# removing twitter mentions

def remove_mentions(text):
    mentions = re.compile(r"(@[A-Za-z0-9]+)")
    return mentions.sub('', text)


# removing html symbols

def remove_html(text):
    html = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    return html.sub('', text)


# removing punctuations and converting UPPERCASE to lowercase

def remove_punctuations(text):
    table = str.maketrans('', '', string.punctuation)
    return text.translate(table).lower()


# removing the stopwords 
# (Stopwords are words which do not add much meaning to the scentence)
# example: a, the, he, you etc.

def remove_stopwords(text):
    s = text.split()
    s = [word for word in s if word not in set(stopwords.words('english'))]
    return ' '.join(s)


# cleaning of the text (CONTAINS ALL THE ABOVE FUNCTIONS)

def text_cleaning(text):
    t = remove_punctuations(remove_html(remove_mentions(remove_emojis(remove_URL(text)))))
    return remove_stopwords(t)




