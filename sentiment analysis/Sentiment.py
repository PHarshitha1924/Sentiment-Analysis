from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Range: -1 (negative) to +1 (positive)

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"
    
    print(f"Input Text: {text}")
    print(f"Sentiment Polarity: {polarity}")
    print(f"Detected Sentiment: {sentiment}\n")

# Run a single example
user_input = input("Enter a sentence to analyze sentiment: ")
analyze_sentiment(user_input)
