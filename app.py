from flask import Flask, render_template, request
import openai

app = Flask(__name__, static_url_path='/assets', static_folder='assets')


# Set your OpenAI API key here
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    # Get the user's question from the form
    question = request.form['question']

    # Make the API request to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=150
    )

    # Extract the answer from the API response
    answer = response.choices[0].message['content']

    return render_template('index.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
