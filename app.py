from flask import Flask, render_template, request
from text_summary import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="main_":
    app.run(debug=True)