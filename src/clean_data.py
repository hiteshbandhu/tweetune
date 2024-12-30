# <------ CONTROL VARIABLES ------>
MAX_CHARS = 100
REMOVE_MENTIONS = True
REMOVE_HASHTAGS = True
REMOVE_WEBLINKS = True
INPUT_PATH = ""
OUTPUT_PATH = ""


# Import necessary library
import pandas as pd

# Load the data
df = pd.read_csv(INPUT_PATH)

# Sort by Impressions
df = df.sort_values('Impressions', ascending=False)

# Filter rows where 'Post text' has more than MAX_CHARS characters
df = df[df['Post text'].str.len() >= MAX_CHARS]

# Extract 'Post text' column and rename it to 'tweet'
df = df[['Post text']].rename(columns={'Post text': 'tweet'})

# Remove quotes from 'tweet' column
df['tweet'] = df['tweet'].str.strip('"')

# Remove ' from the tweets
df['tweet'] = df['tweet'].str.replace("'", '')

# Apply cleaning based on control variables
if REMOVE_MENTIONS:
    df['tweet'] = df['tweet'].str.replace(r'@([A-Za-z0-9_]+)', '', regex=True)

if REMOVE_HASHTAGS:
    df['tweet'] = df['tweet'].str.replace(r'#([A-Za-z0-9_]+)', '', regex=True)

if REMOVE_WEBLINKS:
    df['tweet'] = df['tweet'].str.replace(r'http\S+|www\.\S+', '', regex=True)

# Save cleaned data to output CSV
df.to_csv(OUTPUT_PATH, index=False)

print(f"Cleaned data saved to {OUTPUT_PATH}. The length of the cleaned data is {len(df)}")

