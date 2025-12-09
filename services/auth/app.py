from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Server is up, vibes are good, and life is great!"

@app.route('/health')
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

