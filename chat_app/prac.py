import google.generativeai as genai

genai.configure(api_key="AIzaSyAc7P_EPlzXwVQsDJ4JTg1CRH0ZwdJ-hDY")

# Use a supported model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

response = model.generate_content("Explain how AI works in simple words.")
print(response.text)
