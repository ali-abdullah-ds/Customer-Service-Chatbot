from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS


app = Flask(__name__, 
            static_folder="static",  # Folder for CSS, JS, images
            template_folder="templates" ) # Folder for HTML templates)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)