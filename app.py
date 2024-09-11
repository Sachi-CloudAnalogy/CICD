from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Hello World !! This Page is using CI/CD pipeline...</h1>"

if __name__ == "__main__":
    app.run(debug=True)
   