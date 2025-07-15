from flask import Flask, request, jsonify, render_template
from groq import Groq
import os
import difflib
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

app = Flask(__name__)
groq_client = Groq(api_key=GROQ_API_KEY)


def highlight_differences(original, corrected):
    original_words = original.split()
    corrected_words = corrected.split()
    diff = difflib.ndiff(original_words, corrected_words)
    result = []

    for word in diff:
        if word.startswith('+ '):
            result.append(f'<span class="highlight">{word[2:]}</span>')
        elif word.startswith('- '):
            continue
        elif word.startswith('? '):
            continue
        else:
            result.append(word[2:])

    return ' '.join(result)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/spell_check', methods=['POST'])
def spell_check():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prompt = f"""Please correct the grammar and spelling mistakes in this sentence.
Return only the corrected sentence without any explanations or notes.

Sentence:
{text}
"""

    try:
        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a professional English grammar corrector."},
                {"role": "user", "content": prompt}
            ]
        )

        corrected_text = response.choices[0].message.content.strip()
        highlighted_text = highlight_differences(text, corrected_text)

        return jsonify({
            "original_text": text,
            "corrected_text": corrected_text,
            "highlighted_text": highlighted_text
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
