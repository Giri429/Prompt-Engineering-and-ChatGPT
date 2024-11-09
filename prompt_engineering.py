import openai

# Replace with your actual API key from OpenAI
openai.api_key = "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"

def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

# Prompt for the user
user_prompt = input("Enter your prompt for ChatGPT: ")
print(get_chatgpt_response(user_prompt))
