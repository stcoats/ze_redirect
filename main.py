from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def redirect_home():
    return redirect("https://ycsep-fastapi-viewer-ycsep-test.2.rahtiapp.fi", code=302)