from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, Siva! Your argocd image detect image correctly or not check it once do it again once more and one more thing is now i am checking new version container"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
