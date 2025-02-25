from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "this one final new version which will happen next"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
