from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import requests

app = Flask(__name__)

# FakeStoreAPI endpoint
FAKE_STORE_API = "https://fakestoreapi.com/products"

def recognize_speech():
    """Convert speech to text using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Sorry, the speech service is down."

def search_products(query):
    """Search for products using FakeStoreAPI."""
    response = requests.get(FAKE_STORE_API)
    if response.status_code == 200:
        products = response.json()
        # Filter products based on the query
        filtered_products = [product for product in products if query.lower() in product['title'].lower()]
        return filtered_products
    return []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/voice_search", methods=["POST"])
def voice_search():
    # Step 1: Convert speech to text
    query = recognize_speech()
    # Step 2: Search for products
    products = search_products(query)
    return jsonify({"query": query, "products": products})

if __name__ == "__main__":
    app.run(debug=True)