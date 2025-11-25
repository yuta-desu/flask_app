from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/mypage")
def mypage():
    return "マイページです。"

@app.route("/about")
def about():
    return "会社概要です。"

@app.route("/contact")
def contact():
    return "お問い合わせ画面です。"

if __name__ == "__main__":
    app.run(debug=True)