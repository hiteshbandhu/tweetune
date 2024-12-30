# tweetune

This tool allows you to process tweet data extracted from Twitter Analytics and generate relevant questions based on the content of each tweet. It consists of two main steps: cleaning the tweet data and then generating questions from the cleaned data.

## Overview

1. **Step 1**: Clean and preprocess your tweet data.
2. **Step 2**: Generate questions based on the cleaned tweet data.

### Prerequisites

- Python 3.x
- Required libraries: `pandas`, `groq`

You will also need an **GROQ API key** to generate questions from tweets.

All the code is available in the `src` folder.
---

## Step 1: Clean and Preprocess Tweets

In this step, you will clean and preprocess the tweet data by removing unwanted elements like mentions, hashtags, and URLs. Additionally, tweets shorter than a specified character limit will be filtered out. Use `clean_data.py` for this purpose.

### Requirements

- A CSV file containing tweets downloaded from **Twitter Analytics**. Ensure the file includes a column named `Post text`, which contains the tweet text.
  
### Key Control Variables

- `MAX_CHARS`: Minimum number of characters a tweet must have to be included.
- `REMOVE_MENTIONS`: Set to `True` to remove mentions (`@username`).
- `REMOVE_HASHTAGS`: Set to `True` to remove hashtags (`#hashtag`).
- `REMOVE_WEBLINKS`: Set to `True` to remove URLs (web links).

### Process

1. **Input CSV**: Load the CSV file containing tweets.
2. **Sorting**: Optionally, sort the data by impressions.
3. **Filtering**: Filter out tweets with fewer than `MAX_CHARS` characters.
4. **Cleaning**: Remove mentions, hashtags, and URLs based on control variables.
5. **Output**: Save the cleaned data into a new CSV file.

---

## Step 2: Generate Questions from Cleaned Tweets

After cleaning the tweet data, the next step is to generate questions based on the content of each tweet. Use `generate_questions.py` for this purpose

### Requirements

- The cleaned tweet CSV from **Step 1**.
- An **GROQ API key** to generate questions.

### Process

1. **Input CSV**: Use the cleaned CSV from Step 1.
2. **Question Generation**: The tool will use the OpenAI API to generate relevant questions for each tweet.
3. **Output**: A new CSV will be created containing the original tweet and the generated question.

---

## Example Output

After running the scripts, your final output CSV will include two columns:

| tweet                                      | Generated Question                                       |
|--------------------------------------------|----------------------------------------------------------|
| "I am learning machine learning!"          | "What aspects of machine learning are you focusing on?"   |
| "What's the future of AI?"                 | "How do you envision the future of AI impacting industries?" |
| "How do you use GPT-3 effectively?"        | "What are the best practices for using GPT-3 in applications?" |

---

## Installation and Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/tweet-question-generator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd tweet-question-generator
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Obtain your **GROQ API key** and set it up for use with the question generation script.

---

## Running the Tool

### Step 1: Clean the Tweet Data

Run the cleaning script on your downloaded Twitter Analytics CSV file to preprocess the data:

```bash
python clean_data.py
```

After this step, you’ll have a CSV file with cleaned tweet data.

### Step 2: Generate Questions

Run the question generation script to create questions from your cleaned tweet data:

```bash
python generate_questions.py
```

You will receive a CSV file containing the original tweet and the generated question for each tweet.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Conclusion

By following these steps, you can clean your tweet data and generate meaningful questions that can be used for engagement, analysis, or research purposes. If you encounter any issues or have suggestions for improvements, feel free to open an issue or contribute to the project.
