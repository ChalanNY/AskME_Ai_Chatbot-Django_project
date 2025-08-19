from django.shortcuts import render
import google.generativeai as genai
from dotenv import load_dotenv
import os
import markdown

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


def ask_question(request):
    response_html = ''
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            try:
                response = model.generate_content(question)
                markdown_text = response.text
                response_html = markdown.markdown(markdown_text)  # ✅ Convert to HTML
            except Exception as e:
                response_html = f"<p>Error: {str(e)}</p>"

    return render(request, 'index.html', {'response': response_html})
