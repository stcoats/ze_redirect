from flask import Flask, redirect

app = Flask(__name__)

TARGET_URL = "https://ze-ze.2.rahtiapp.fi/zipfexplorer"  # ← change this

@app.route("/")
def redirect_root():
    return redirect(TARGET_URL, code=302)

@app.route("/zipfexplorer")
def redirect_zipfexplorer():
    return redirect(TARGET_URL, code=302)

# Optional: catch all other paths
@app.route("/<path:other>")
def catch_all(other):
    return redirect(TARGET_URL, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
