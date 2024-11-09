from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'your-api-key' with your OpenAI API key
openai.api_key = 'your-api-key'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the user's query
@app.route('/ask', methods=['POST'])
def ask():
    user_prompt = request.form['user_prompt']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_prompt,
        max_tokens=100
    )
    answer = response.choices[0].text.strip()
    return render_template('index.html', user_prompt=user_prompt, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
