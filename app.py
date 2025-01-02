from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS
import toml

with open("config.toml", "r") as config_file:
    config = toml.load(config_file)


app = Flask(__name__, 
            static_folder="static",  # Folder for CSS, JS, images
            template_folder="templates" ) # Folder for HTML templates)

CORS(app, resources={r"/*": {"origins": config["app"]["cors_allowed_origins"]}})

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


if __name__ == "__main__":
    app.run(debug=config["flask"]["debug"], host=config["flask"]["host"], port=config["flask"]["port"])