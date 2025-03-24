MrBeast YouTube Channel Analysis 📊🎥
This project analyzes MrBeast's YouTube videos using the YouTube API and various Python libraries. It gathers data such as video transcriptions, metrics, sentiment analysis, word counts, and more, to provide insights into the content and popularity of his videos.

Technologies and Libraries Used 🛠️
This project utilizes several Python libraries and tools to interact with YouTube, process data, and generate visualizations:

File Management and Environment Variables 🌐
google.colab: Enables uploading and downloading files within Google Colab.

dotenv: Loads environment variables from .env files (e.g., API keys).

os: Interacts with the operating system to handle paths and variables.

Interacting with YouTube API 🎬
googleapiclient.discovery: Connects with the YouTube API to fetch video details, comments, and more.

youtube_transcript_api: Retrieves YouTube video transcriptions.

Data Management 📊
pandas: Handles tabular data (DataFrames) for analysis.

json: Works with JSON data (key-value pairs).

requests: Makes HTTP requests to APIs.

Image and Video Processing 🖼️📹
PIL: Manipulates images (open, edit, convert).

numpy: Handles arrays and numerical operations.

cv2: Image and video processing (e.g., face detection).

io.BytesIO: Converts binary data into manageable objects.

Sentiment Analysis and Text Processing 🧠💬
nltk: Natural Language Processing library.

SentimentIntensityAnalyzer: Performs sentiment analysis on text (positive, negative, or neutral).

stopwords: Filters out common words (stopwords) that don’t contribute to text analysis.

NoSQL Database (MongoDB) 💾
pymongo: Connects and manages NoSQL databases in MongoDB Atlas.

certifi: Verifies SSL certificates when connecting to MongoDB.

Data Visualization 📈
seaborn & matplotlib: Used for creating statistical graphs and custom visualizations.

plotly: Creates interactive, advanced visualizations.

wordcloud: Generates word clouds from text.

Text Analysis 🔠
sklearn.feature_extraction.text: Converts text into numerical vectors for text analysis.

Transcription Management 📝
tqdm: Displays a progress bar during long tasks.

concurrent.futures: Executes functions in parallel to improve performance.

Installation 🔧
To install all necessary dependencies, run the following commands:

bash
Copy
Edit
!pip install -q dotenv
!pip install -q isodate
!pip install -q youtube_transcript_api
!pip install -q nltk
!pip install -q pymongo
!pip install -q seaborn
!pip install -q plotly
!pip install -q wordcloud
Fetching Data from YouTube 🎥
1. Fetching Video Data 📈
Use the YouTube API to extract basic video data (such as views, duration, etc.). You need to configure your Google Cloud project and obtain an API Key.

Code to fetch video data:

python
Copy
Edit
from googleapiclient.discovery import build

# Set up your YouTube API Key
api_key = 'YOUR_API_KEY'

# Connect to the YouTube API
youtube = build('youtube', 'v3', developerKey=api_key)

# Get list of videos from a specific channel
def get_video_data(channel_id):
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        maxResults=50
    )
    response = request.execute()
    return response
2. Fetching Transcriptions 📝
Use the YouTube Transcript API to fetch video transcriptions:

python
Copy
Edit
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcription(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        return str(e)
Data Analysis from Transcriptions 🔍
Sentiment Analysis 😊😞
We use VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze sentiment from the transcriptions (positive, neutral, or negative).

python
Copy
Edit
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Sentiment analysis on video transcriptions
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    return sia.polarity_scores(text)['compound']
Grammatical Analysis 📝
To analyze the text, we count the number of verbs, adjectives, and nouns in each transcription using NLTK.

python
Copy
Edit
from nltk import pos_tag
from nltk.tokenize import word_tokenize

def count_verbs_adjectives(text):
    words = word_tokenize(text)
    tagged = pos_tag(words)
    verbs = [word for word, tag in tagged if tag.startswith('VB')]
    adjectives = [word for word, tag in tagged if tag.startswith('JJ')]
    nouns = [word for word, tag in tagged if tag.startswith('NN')]
    return len(verbs), len(adjectives), len(nouns)
Calculating Average Word Count 🧮
We calculate the average number of words per video, as well as the average number of unique words and the overall sentiment:

python
Copy
Edit
df_videos['word_count'] = df_videos['transcription'].apply(lambda x: len(word_tokenize(x)) if isinstance(x, str) else 0)
average_word_count = df_videos['word_count'].mean()
Data Visualization 📊
We use libraries like Seaborn and Matplotlib to create visualizations of the word counts, sentiment, and other analyses.

Average Sentiment Chart 📊
python
Copy
Edit
import seaborn as sns
import matplotlib.pyplot as plt

# Bar chart for average sentiment by video type (shorts vs non-shorts)
sns.barplot(x='short', y='sentiment', data=df_videos, palette='viridis')
plt.title('Average Sentiment by Video Type')
plt.show()
MongoDB NoSQL Database 💾
If you want to store the data in a NoSQL database, use MongoDB to store video information, transcriptions, and analysis results.

python
Copy
Edit
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://username:password@hostname:port/")
db = client['mrbeast_youtube']
collection = db['videos']

# Insert a document into MongoDB
collection.insert_one({'video_id': '12345', 'title': 'MrBeast Video', 'views': 1000000})
Conclusion 🎉
This project allows you to extract data from MrBeast's YouTube videos, process the transcriptions, and perform advanced sentiment, grammatical, and popularity analysis. Results can be visualized using charts and exported for deeper analysis.
