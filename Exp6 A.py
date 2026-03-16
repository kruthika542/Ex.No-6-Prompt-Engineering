from openai import OpenAI
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download sentiment model
nltk.download('vader_lexicon')

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

# Persona Pattern Prompt
prompt = """
Act as a professional technology reviewer.
Write a short review about a new smartphone with a powerful battery and AI camera.
"""

# Step 1: Generate text using AI tool
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

generated_text = response.output[0].content[0].text

print("Generated Review:\n")
print(generated_text)

# Step 2: Sentiment analysis using another AI tool
sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(generated_text)

print("\nSentiment Analysis:")
print(sentiment)

# Step 3: Generate simple insights
if sentiment['compound'] > 0:
    print("\nInsight: The product review is positive and suitable for marketing promotion.")
else:
    print("\nInsight: The review tone is neutral/negative and may require improvement.")