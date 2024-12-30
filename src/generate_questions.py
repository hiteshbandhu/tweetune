import os
import pandas as pd
import json
from groq import Groq
from tqdm import tqdm  # For progress visualization

# Initialize Groq client function
def groq_client_chat(messages, model="llama3-70b-8192"):
    client = Groq(api_key="") # Add your API key here
    
    # Send a chat completion request to the Groq model
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    
    # Return the generated content from the response
    return chat_completion.choices[0].message.content

# Function to process the input CSV and generate questions for each tweet
def process_tweets(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Prepare a list to hold the extracted questions and tweets
    extracted_data = []

    # Process the tweets in batches of 20
    batch_size = 20
    total_batches = len(df) // batch_size + (1 if len(df) % batch_size != 0 else 0)

    # Loop through the batches
    for batch_idx in tqdm(range(total_batches), desc="Processing batches", unit="batch"):
        # Get the current batch of tweets
        start_idx = batch_idx * batch_size
        end_idx = min((batch_idx + 1) * batch_size, len(df))
        batch = df.iloc[start_idx:end_idx]
        
        # Format the tweets into a single string for the system prompt
        tweets = "\n".join([tweet for tweet in batch['tweet']])
        
        # Create the system prompt
        system_prompt = f"""
        You are tasked with generating relevant questions based on the tweets provided below. 
        Each tweet should have one clear, insightful question that targets the key points or details of the tweet. The output should be JSON only and in the format of "Input" and "Output" pairs. The "Input" should be the tweet, and the "Output" should be the question you generate. Don't include any additional information in the output. 


        Tweets:
        {tweets}

        Questions:
        """

        # Send the full prompt to the Groq model using the client function
        response = groq_client_chat([
            {"role": "system", "content": "Only output the asked JSON and nothing else. No additonal text. No confirmations."},
            {"role": "user", "content": system_prompt}
        ])
        
        # Parse the JSON response (expecting a JSON string with question-output pairs)
        try:
            parsed_response = json.loads(response)
            # Extract the input-output pairs and add them to the list
            for entry in parsed_response:
                extracted_data.append({
                    "Input": entry.get("Input"),
                    "Output": entry.get("Output")
                })
        except json.JSONDecodeError:
            print(f"Error parsing JSON response: {response}")
            continue

    # Create a new DataFrame with the extracted data
    output_df = pd.DataFrame(extracted_data)

    # Save the results into a new CSV file
    output_df.to_csv(output_file, index=False)

    print(f"Output saved to {output_file}")

# Run the function
input_file = 'xyz.csv'  # Path to your input CSV file
output_file = 'xyz.csv'  # Path to your output CSV file
process_tweets(input_file, output_file)
