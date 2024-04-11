from flask import Flask, render_template
from flask_wtf import FlaskForm



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)