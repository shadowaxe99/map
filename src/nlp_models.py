```python
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class NLPModel:
    def __init__(self):
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.vectorizer = CountVectorizer()
        self.encoder = LabelEncoder()
        self.classifier = MultinomialNB()

    def analyze_sentiment(self, userInput):
        sentiment_score = self.sentiment_analyzer.polarity_scores(userInput)
        return sentiment_score

    def extract_entities(self, userInput):
        tokenized_sentence = sent_tokenize(userInput)
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(userInput)
        words_filtered = [word for word in words if word not in stop_words]
        return words_filtered

    def recognize_intent(self, userInput, userPreferences):
        X = self.vectorizer.fit_transform(userInput)
        y = self.encoder.fit_transform(userPreferences)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.classifier.fit(X_train, y_train)
        intent = self.classifier.predict(X_test)
        return intent
```