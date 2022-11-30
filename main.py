from flask import Flask
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

app.run(host="0.0.0.0", port=80)
