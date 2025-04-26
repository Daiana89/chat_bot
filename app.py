import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

app = Flask(__name__)

model = genai.GenerativeModel('gemini-2.0-flash')

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            # Solicitar contenido a la API de Gemini basado en el input del usuario
            response = model.generate_content(user_input)
            response_text = response.text
        except Exception as e:
            response_text = f"Error: {str(e)}"
    
    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
